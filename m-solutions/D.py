n = int(input())
a = []
b = []
for i in range(n-1):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)

c = list(map(int, input().split()))
c.sort()
s = 0
for i in range(len(c)-1):
    s += c[i]

print(s)
c = c[:-1]
print(c)
for i in c:
    print(i)
