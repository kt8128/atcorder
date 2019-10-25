n = int(input())
# happy[i][j] : i日めにjをした。(j=0:a, j=1:b, j=2:c)
happy = [[0, 0, 0] for i in range(n)]
for i in range(n):
    a,b,c = map(int, input().split())
    if i == 0:
        happy[0][0] = a
        happy[0][1] = b
        happy[0][2] = c
    else:
        happy[i][0] = max(happy[i-1][1], happy[i-1][2]) + a
        happy[i][1] = max(happy[i-1][0], happy[i-1][2]) + b
        happy[i][2] = max(happy[i-1][0], happy[i-1][1]) + c

print(max(happy[n-1][0], happy[n-1][1], happy[n-1][2]))
