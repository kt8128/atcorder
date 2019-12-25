from collections import Counter

n = int(input())
c = Counter(list(map(int, input().split())))
for a in c.values():
    if a >= 4:
        print("YES")
        break
else:
    print("NO")
