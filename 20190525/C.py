N, M = map(int, input().split())
Ln = []
Rn = []
for i in range(M):
    L, R = map(int, input().split())
    Ln.append(L)
    Rn.append(R)

target = []
target_candidate = []
for i in range(M):
    target_candidate = Ln[i:] + Rn[:i+1]
    if target == []:
        target = target_candidate
    else:
        target = [s for s in target if s in target_candidate]

print(len(set(target)))
