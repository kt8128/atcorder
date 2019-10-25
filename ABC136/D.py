import copy

S = list(input())
ans = ['1'] * len(S)
# split_num = [0]
# for i, s in enumerate(S[1:-1]):
#     if S[i-1] == "L" and S[i+1] == "R":
#         ans[i] = 0
#         split_num.append(i)
# split_num.append(len(S))
# #
# for i in range(len(split_num)-1):
#     for i, s in enumerate(S[split_num[i]:split_num[i+1]]):
#         print(s)

pre_ans = ['1'] * len(S)
pre_pre_ans = ['1'] * len(S)
flag = 0
# while True:
for k in range(1, 10 ** 2):
    ans[0] = '0'
    ans[-1] = '0'
    if S[1] == 'L':
        ans[0] = pre_ans[1]
    if S[-2] == "R":
        ans[-1] = pre_ans[-2]
    for i, s in enumerate(S[1:-1]):
        ans[i+1] = '0'
        if S[i] == 'R' and S[i+2] == "L":
            ans[i+1] = str(int(pre_ans[i]) + int(pre_ans[i+2]))
        elif S[i] == 'R':
            ans[i+1] = pre_ans[i]
        elif S[i+2] == 'L':
            ans[i+1] = pre_ans[i+2]
    if ans == pre_ans:
        flag = 1
        break
    elif ans == pre_pre_ans:
        if k % 2 == 0:
            flag = 1
        else:
            flag = 2
        break
    pre_pre_ans = copy.deepcopy(pre_ans)
    pre_ans = copy.deepcopy(ans)

if flag == 1:
    print(' '.join(ans))
elif flag == 2:
    print(' '.join(pre_ans))
