n = int(input())
s = list(input())
count = 0
pre = s[0]
for i in s[1:]:
    if pre != i:
        count += 1
        pre = i

print(count+1)
