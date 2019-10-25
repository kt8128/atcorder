N = int(input())
list = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    list.append([S, 100-P, i+1])

new_list = sorted(list, key=lambda x: (x[0], x[1]))
for k in new_list:
    print(k[2])
