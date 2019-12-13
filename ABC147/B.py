s = input()
ans = 0
for i in range(0, len(s)//2):
    if list(s)[i] != list(s)[len(s)-i-1]:
        ans += 1
print(ans)
