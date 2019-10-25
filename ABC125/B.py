N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum([ max( 0, (V[i]-C[i]) ) for i in range(N) ])

print(ans)
