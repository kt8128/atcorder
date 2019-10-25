import collections

n = int(input())
S = []
count = 0
for _ in range(n):
    S.append(''.join(sorted(list(input()))))

for i, v in collections.Counter(S).items():
    for i in range(1, v):
        count += i

print(count)
