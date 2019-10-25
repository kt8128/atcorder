n = int(input())
L = list(map(int, input().split()))
L.sort()
count = 0

for i, l1 in enumerate(L):
    for k, l2 in enumerate(L[i+1:]):
        num = i + k + 2
        for l3 in L[num:][::-1]:
            if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
                count += 1
            else:
                break

print(count)
