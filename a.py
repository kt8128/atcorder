def fizzbuzz(num):
    for i in range(1, num+1):
        if i % 15 == 0:
            print("fizz buzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)

# fizzbuzz(30)

def feb(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return feb(num-1) + feb(num-2)

# print(feb(6))


def rev(n):
    ans = []
    while n >= 1:
        ans.append(n % 10)
        n = n // 10
    b = 0
    for i, a in enumerate(ans):
        b += 10 ** (len(ans)-i-1) * a
    return b

def rev1(n):
    ans = 0
    while n >= 1:
        ans = ans * 10 + n % 10
        n = n // 10

print(rev(123))
