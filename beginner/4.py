N = int(input())
A = list(map(int, input().split()))
counter = 0
for i in range(100):
    if all([x % 2 == 0 for x in A]):
        A = list(map(lambda x: round(x/2), A))
        counter += 1
print(counter)
