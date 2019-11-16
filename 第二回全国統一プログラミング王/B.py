def input():
    import sys
    return sys.stdin.readline().strip()


def main():
    from collections import defaultdict
    d = [input() for _ in range(2)]
    n = d[0]
    d = list(map(int, d[1].split(' ')))
    d.sort()
    mod = 998244353
    if d[0] != 0 or d.count(0) != 1:
        print(0)
    else:
        count = 1
        dc = defaultdict(int)
        for i in d[1:]:
            dc[i] += 1
        for i in range(1, d[-1]):
            count = ((count % mod) * ((dc[i]**dc[i+1]) % mod)) % mod
        print(count % mod)


if __name__ == '__main__':
    main()
