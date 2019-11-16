s = input()
for i in range(len(s)):
    if i % 2 == 0:
        if not (s[i] == 'R' or s[i] == 'U' or s[i] == 'D'):
            print('No')
            break
    else:
        if not (s[i] == 'L' or s[i] == 'U' or s[i] == 'D'):
            print('No')
            break
else:
    print('Yes')
