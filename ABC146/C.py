A, B, X = map(int, input().split())
ans = 0
d = len(list(str(X)))

if X >= A * (10 ** 9) + B * (10):
    print(10 ** 9)
    exit()
elif A > X or B > X:
    print(0)
    exit()

temp = 0
temp1 = 0

def binary_search(n):
    global temp1
    global temp
    dn = len(list(str(n)))
    a = A * n + B * dn
    if temp1 == n:
        print(n)
        return
    temp1 = n
    if a > X:
        temp = n
        binary_search(n//2)
    else:
        binary_search((n+temp)//2)


binary_search(X//2)
