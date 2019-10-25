import random
import itertools

N, M = map(int, input().split())

s = []
p = []
for i in range(M):
    s.append(list(map(int, input().split())))

p = list(map(int, input().split()))

off = []
switch = []
pro = 1
r = ()

def iter_odd(s, length):
    on = []
    if length % 2 == 0:
        for k in range(length//2+1):
            n = 2 * k + 1
            for element in itertools.combinations(s[i][1:], n):
                on.append(element)
    else:
        for k in range(length//2+1):
            n = 2 * k + 1
            for element in itertools.combinations(s[i][1:], n):
                on.append(element)
    return on

def iter_even(s, length):
    on = []
    if length % 2 == 0:
        for k in range(length//2+1):
            n = 2 * k
            for element in itertools.combinations(s[i][1:], n):
                on.append(element)
    else:
        for k in range(length//2+1):
            n = 2 * k
            for element in itertools.combinations(s[i][1:], n):
                on.append(element)
    return on

for i in range(M):
    print(s[i])
    length = len(s[i][1:])
    on = []
    if p[i] == 0:
        on = iter_even(s, length)
    else:
        on = iter_odd(s, length)

    print(on)
    for ele in on:
        sw = [0] * N
        for e in ele:
            sw[e-1] = 1
        switch.append(sw)
    print(switch)
