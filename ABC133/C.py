l, r = map(int, input().split())
m = 100000000
flag = 0
if r - l > 2019:
    flag = 1
for i in range(l, l+2019):
    m = min(m, i*)

if flag == 0:
    a = (l % 2019) * ((l+1) % 2019) % 2019
    print(a)
elif flag == 1:
    print(0)
