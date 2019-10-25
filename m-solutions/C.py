from fractions import Fraction


n, a, b, c = list(map(int, input().split()))
x = 10**9 + 7
a = Fraction(a,100)
b = Fraction(b,100)
c = Fraction(c,100)
kitaiti = Fraction(0,1)
a1 = a.numerator
a2 = a.denominator
b1 = b.numerator
b2 = b.denominator
c1 = c.numerator
c2 = c.denominator
# a = x.numerator
#
# # 分母を取得します
# b = x.denominator

for i in range(100000):
    # (i+n)*((c**i)*(a**n) + (c**i)*(b**n))
    f1 = Fraction((c1**i)*(a1**n), (c2**i)*(a2**n))
    f2 = Fraction((c1**i)*(b1**n), (c2**i)*(b2**n))
    f = f1 + f2
    print(f)
    kitaiti += Fraction((i+n)*f.numerator, (1+n)*f.denominator)
    # print(kitaiti)
print(round(kitaiti, 10).as_integer_ratio())
p, q = round(kitaiti, 10).as_integer_ratio()[0], round(kitaiti, 3).as_integer_ratio()[1]

for i in range(x-1):
    print(i * q % x == p)
    if  i * q % x == p:
        print(i)
        break
