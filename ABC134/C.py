n = int(input())
max1 = 0
max2 = 0
index = 0
for i in range(n):
    a = int(input())
    new_max = max(a, max1)
    if (a == new_max and max2 <= max1) or (a == new_max and max2 <= max1 and a == max1):
        max2 = max1
        index = i
    elif (a != new_max and max2 <= a) or (a != new_max and max2 <= a and a == max1):
        max2 = a
    max1 = new_max

for i in range(n):
    if i != index:
        print(max1)
    else:
        print(max2)
