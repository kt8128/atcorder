import bisect

x = list(input())
x.sort()
idx = bisect.bisect_left(x, '1')
ans = ''
ans = x[idx] + '0' * idx + ''.join(x[idx+1:])
print(ans)
