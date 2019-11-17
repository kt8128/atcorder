n = int(input())
s = input()
if n % 2 != 0:
    print("No")
else:
    if "".join(list(s[:int(n/2)])) == "".join(list(s[int(n/2):])):
        print('Yes')
    else:
        print('No')
