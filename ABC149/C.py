def is_prime2(q,k=100):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    for i in range(3,k):
        x,y = q,i
        while y:
            x, y =  y, x % y
        if x != 1: continue
        if pow(i, q-1, q) != 1:
            return False
    return True

c = int(input())
for i in range(c, 10**6):
    if is_prime2(i):
        print(i)
        break
