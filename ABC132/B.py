n = int(input())
l = list(map(int, input().split()))
pre_pre = l[0]
pre = l[1]
count = 0
for i in range(2, n):
    cur = l[i]
    if pre_pre < pre < cur or cur < pre < pre_pre:
        count += 1
    pre_pre = pre
    pre = cur
print(count)
