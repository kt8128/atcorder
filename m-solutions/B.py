b = input()
win = b.count('o')
l = len(b)


if 8-win <= 15-l:
    print('YES')
else:
    print("NO")
