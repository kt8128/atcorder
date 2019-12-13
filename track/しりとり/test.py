import sys
import collections
import itertools
import pulp

# ソース（始まり）とシンク（終わり）
SOURCE = u"s"
SINK = u"t"

## 指定した点を通る閉路を1つ見つける関数
## 見つけた閉路は edges から除かれる (見つからなければそのまま)
def one_cycle(edges, start):
    path = [start]
    # 深さ優先探索（スタック）
    # start からの枝を列挙
    stack = [e[1] for e, cnt in edges.iteritems() if e[0] == start and cnt > 0]
    while len(stack) > 0:
        # 枝を1つ選ぶ
        e_new = (path[-1], stack[-1])
        edges[e_new] -= 1
        path.append(stack[-1])
        # 元の点に戻れたら終了
        if stack.pop() == start:
            return path
        # 今の地点から始まる枝を列挙
        dest_avail = [e[1] for e, cnt in edges.iteritems() if e[0] == e_new[1] and cnt > 0]
        if len(dest_avail) == 0:
            # 行き止まり: 1ステップ巻き戻す
            edges[e_new] += 1
            path.pop()
        else:
            # 行き先を列挙する
            stack += dest_avail
    # 閉路見つからず
    return None

## Euler 閉路を取り出す
def euler_cycle(edges, start):
    edges_tmp = edges.copy()
    # まず1個閉路を探す: 深さ優先探索 (edges_tmp から取り出した閉路が除かれる)
    cycle = one_cycle(edges_tmp, start)
    assert cycle is not None
    cycle_add = cycle
    while len(edges_tmp) > 0:
        # 閉路上の点のうち、出ていく枝の残っているものを選ぶ
        next_start = [v for v in set(cycle) if any(e[0] == v and cnt > 0 for e, cnt in edges_tmp.iteritems())]
        if len(next_start) == 0:
            # 別の連結成分があるので、諦める
            break
        else:
            # 別の閉路を探せ
            cycle_add = one_cycle(edges_tmp, next_start[0])
            assert cycle_add is not None
            # 選んだ開始点で元の閉路とつなげる
            idx = cycle.index(next_start[0])
            cycle = cycle[:idx] + cycle_add + cycle[idx+1:]
    return cycle

# solver の初期化と制約条件の設定
def make_solver(edges, vertexes, constraints):
    solver = pulp.LpProblem("Shiritori", pulp.LpMaximize)

    # 各枝に流すフローが変数に相当
    # 整数変数
    variables = dict((e, pulp.LpVariable(e, lowBound=0, cat="Integer")) for e in edges.keys())

    # 目的関数: フロー総和最大
    solver += sum(variables.values())

    # 制約条件
    # ソースから出るフロー、シンクに入るフローは1
    solver += sum([variables[e] for e in edges if e[0] == SOURCE]) == 1
    solver += sum([variables[e] for e in edges if e[1] == SINK]) == 1

    # 頂点ごとに出るフローと入るフローの総和が一致 (s, t以外)
    for v in vertexes:
        solver += sum([variables[e] for e in edges if e[0] == v]) \
               == sum([variables[e] for e in edges if e[1] == v])

    # フロー量制限
    for e, maxflow in edges.items():
        solver += 0 <= variables[e] <= maxflow

    # 分枝限定法に関する制約条件の追加
    # 「cycle に含まれる点から、それ以外の点への遷移が1つ以上ある」
    for cons in constraints:
        solver += sum(variables[e] for e in cons) >= 1

    return solver, variables


def main(lines):
    n = lines[0]
    words = lines[1].split()
    edges = collections.defaultdict(int)
    edges_word = collections.defaultdict(set)
    for word in words:
        t = (word[0], word[-1])
        edges[t] += 1
        edges_word[t].add(word)

    vertexes = set(itertools.chain(edges.keys()))
    for v in vertexes:
        edges[(SOURCE, v)] = 1
        edges[(v, SINK)] = 1

    length_tmp = 0
    solution_tmp = None
    constraints = []
    while True:
        solver, variables = make_solver(edges, vertexes, constraints)
        solver.solve()
        if solver.status != pulp.constants.LpStatusOptimal:
            # そのような解は無い: 現時点の解が最終的な解
            break

        # sから出る枝とtに入る枝を除いたものが、
        # （飛び地がないと仮定した場合の）しりとりの長さ（単語数）
        length_upper = int(pulp.value(solver.objective)+0.01) - 2

        # *****
        # 結果を加工

        # 使う枝を列挙
        # 簡単のため t -> s のパスを加えて閉路にしておく
        edges_sub = dict(itertools.ifilter(lambda sol: sol > 0, ((e, variables[e].value()) for e in edges.keys())))
        edges_sub[(SINK, SOURCE)] = 1

        # Euler 閉路を探す（どこから始めてもよいのでsに固定）
        cycle = euler_cycle(edges_sub, SOURCE)
        # cycle: s -> X1 -> ... -> Xn -> t -> s で、X1からXnまでの -> の数は len(cycle)-4
        length_lower = len(cycle) - 4
        print >>sys.stderr, length_lower, "/", length_upper,
        if length_lower == length_upper:
            # 連結グラフ
            print >>sys.stderr, "連結グラフ"
            if length_tmp < length_lower:
                # 解の更新
                length_tmp = length_lower
                solution_tmp = cycle
            # 今の解で確定
            break
        else:
            # 連結グラフでない
            # 解の更新ができないなら終わり
            print >>sys.stderr, "非連結グラフ"
            if length_upper <= length_tmp:
                break
            if length_tmp < length_lower:
                # 少なくとも今の解より良い解は見つかった
                length_tmp = length_lower
                solution_tmp = cycle
            print >>sys.stderr, "新たな解の探索を試みます"

            # 次回以降「cycle に含まれる点から、それ以外の点への遷移が1つ以上ある」
            # という条件を追加
            vertexes_cycle = [v for v in vertexes if v in cycle]
            vertexes_outofcycle = [v for v in vertexes if v not in cycle]
            # そのような遷移を列挙
            list_added_edges = [e for e in itertools.product(vertexes_cycle, vertexes_outofcycle) if e in edges]
            if len(list_added_edges) == 0:
                # 初めからそのような遷移がなければ終了
                break
            constraints.append(list_added_edges)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
