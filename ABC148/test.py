a = 2  # 初項 5
d = 2  # 公差 3
n = 250 # 項数 10
p = 1  # 積

for i in range(1, n + 1):
    m = a + (d * (i - 1))
    p *= m
ans = 0
for i in list(str(p))[::-1]:
    if i == '0':
        ans += 1
    else:
        break
print(ans)
