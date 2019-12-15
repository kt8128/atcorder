import copy

N, M = map(int, input().split())
X_Y = []
label = [0] * N
for i in range(M):
    X, Y, Z = map(int, input().split())
    X_Y.append([X, Y])
# print(X_Y)
new_X_Y = X_Y
cost = 0
while new_X_Y:
    counter = [0] * N
    for a in new_X_Y:
        for b in a:
            counter[b-1] += 1
    index = counter.index(max(counter))
    rem = index+1
    # print("rem:{}".format(rem))
    new_X_Y = []
    for e in copy.copy(X_Y):
        if rem not in e:
            new_X_Y.append(e)
        else:
            label[e[0]-1] = 1
            label[e[1]-1] = 1
    X_Y = new_X_Y
    cost += 1
    # print(new_X_Y)
# print(label)
count = 0
flag = 0
for i in label:
    if i == 0:
        count += 1
        flag = 1
if flag == 0:
    cost -= 1
print(cost+count)
