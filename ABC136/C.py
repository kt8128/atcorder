n = int(input())
H = list(map(int, input().split()))

max_h = 0
ans = 'Yes'
for h in H:
    if max_h < h:
        max_h = h

    if max_h - 1  > h:
        ans = "No"
        break

print(ans)
