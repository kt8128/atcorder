from collections import defaultdict
d = defaultdict(int)
s = input()
for c in s:
    d[c] += 1

flag = 0
for k, v in d.items():
    if v != 2:
        flag = 1

if flag == 1:
    print('No')
else:
    print('Yes')
