x, y = map(int, input().split())
ans = 0
root = []
root.append([x, y])
m = 'l'
flag = 0
cnt = 0
if (x+y) % 3 != 0:
    print(0)
else:
    r = 0
    while True:
        print(root)
        print(m)
        if len(root) == 1:
            cnt += 1
        if cnt == 3:
            break
        if len(root) == 0:
            ans = 0
            break
        if m == 'l':
            t = [root[0][0]-2, root[0][1]-1]
            root.insert(0, t)
        else:
            t = [root[0][0]-1, root[0][1]-2]
            root.insert(0, t)
            r += 1
            m = 'l'
        if root[0] == [0, 0]:
            root.pop(0)
            if m == 'r':
                pass
            else:
                m = 'r'
                for _ in range(r):
                    root.pop(0)
                r = 0
            ans += 1
        elif sum(root[0]) < 3:
            root.pop(0)
            if m == 'r':
                pass
            else:
                m = 'r'
                for _ in range(r):
                    root.pop(0)
                r = 0
        elif (root[0][0] <= 1 and root[0][1] > 2) or (root[0][1] <= 1 and root[0][0] > 2):
            root.pop(0)
            if m == 'r':
                pass
            else:
                m = 'r'
                for _ in range(r):
                    root.pop(0)
                r = 0
        ans = ans % (10 ** 9 + 7)
print(ans)
