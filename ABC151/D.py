H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))
ans = 0
for h1 in range(H):
    for w1 in range(W):
        if S[h1][w1] == '.':
            START = (h1, w1, 0)
            for h2 in range(H):
                for w2 in range(W):
                    GOAL = (h2, w2)
                    stack = [START]
                    check = [(h1, w1)]
                    cnt = 0
                    ans1 = H*W-1
                    while stack:
                        h, w, cnt = stack.pop()
                        if (h, w) == GOAL and ans1 > cnt:
                            ans1 = cnt
                            continue
                        if 0 <= h < H-1 and S[h+1][w] == '.' and (h+1, w) not in check:
                            check.append((h+1, w))
                            stack.append((h+1, w, cnt+1))
                        if 0 < h <= H-1 and S[h-1][w] == '.' and (h-1, w) not in check:
                            check.append((h-1, w))
                            stack.append((h-1, w, cnt+1))
                        if 0 <= w < W-1 and S[h][w+1] == '.' and (h, w+1) not in check:
                            check.append((h, w+1))
                            stack.append((h, w+1, cnt+1))
                        if 0 < w <= W-1 and S[h][w-1] == '.' and (h, w-1) not in check:
                            check.append((h, w-1))
                            stack.append((h, w-1, cnt+1))
                    if ans < ans1:
                        ans = ans1
print(ans)
