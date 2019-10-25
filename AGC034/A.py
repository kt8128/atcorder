n,a,b,c,d = map(int, input().split())
s = input()

rock = 0
max_rock = []
non = 0
max_non = []
k = 0
for i in s:
    if i == '#':
        rock += 1
        if non >= 3:
            max_non.append([non, k])
        non = 0
    else:
        non += 1
        if rock >= 2:
            max_rock.append([rock, k])
        rock = 0
    if k == n-1:
        k += 1
        if non >= 3:
            max_non.append([non, k])
        if rock >= 2:
            max_rock.append([rock, k])
    k += 1

# print(max_non)
max_non1 = [i for i in max_non if (i[1]-i[0]+2 < d and i[1]-i[0] > b) or (i[1] > b and i[1] < d) or i[1] > b]
# max_rock1 = [i for i in max_rock if (i[1] < d and i[1] < c and i[1] > a and i[1] > b) or (i[1])]
max_rock1 = [i for i in max_rock if (i[1] > a and i[1] < b) or (i[1] > b and i[1] < c) or (i[1] > c and i[1] < d)]
max_rock3 = [i for i in max_rock if (i[1] > a and i[1] < b) or (i[1] > b and i[1] < d) or (i[1] > d and i[1] < c)]
max_rock2 = [i for i in max_rock if (i[1] < d and i[1] > b) or (i[1] > a and i[1] < c)]
# print(max_non1)
# print(max_rock1)
if b > c:
    if len(max_rock2) > 0:
        print('No')
    else:
        print('Yes')
elif c > d:
    if len(max_rock3) > 0:
        print('No')
    elif len(max_non1) > 0:
        print('Yes')
    else:
        print('No')
elif len(max_rock1) > 0:
    print('No')
else:
    print('Yes')
