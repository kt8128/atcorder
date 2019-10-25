s = input()
a = s[::2].count('1') + s[1::2].count('0')
b = s[::2].count('0') + s[1::2].count('1')
print(min(a,b))
