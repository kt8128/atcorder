import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    ac = 0
    wa = 0
    b = defaultdict(lambda: 0)
    for _ in range(m):
        q, j = input().split()
        if b[q] != -1 and j == 'AC':
            ac += 1
            if q in b:
                wa += b[q]
                b[q] = -1
        else:
            if b[q] != -1:
                b[q] += 1
    print(ac, wa)

if __name__ == "__main__":
    main()
