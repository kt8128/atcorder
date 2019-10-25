import re
import math

def fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

n,m = map(int, input().split())
step = ['0']*(n+1)
for i in range(m):
    a = int(input())
    step[a] = '1'
steps = ''.join(step)

a = re.findall('000*', steps)
b = len(re.findall('11', steps))
# print(steps)
count = 1
for i in a:
    count *= fib(len(i)+1) % 1000000007

if b != 0:
    print(0)
else:
    print(count % 1000000007)
