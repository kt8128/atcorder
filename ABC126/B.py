l = list(input())

ab = l[0] + l[1]
cd = l[2] + l[3]

if ab[0] == "0":
    ab = ab[1]
if cd[0] == "0":
    cd = cd[1]

ab = int(ab)
cd = int(cd)
if ab < 13 and cd < 13 and ab != 0 and cd != 0:
    print("AMBIGUOUS")
elif ab >= 13 and cd < 13 and ab != 0 and cd != 0:
    print("YYMM")
elif cd >= 13 and ab < 13 and ab != 0 and cd != 0:
    print("MMYY")
elif ab == 0 and cd == 0:
    print("NA")
elif ab >= 13 and cd >= 13:
    print("NA")
elif ab == 0 and cd < 13 and cd != 0:
    print("YYMM")
elif cd == 0 and ab < 13 and ab != 0:
    print("MMYY")
elif ab == 0 and cd >= 13 and cd != 0:
    print("NA")
elif cd == 0 and ab >= 13 and ab != 0:
    print("NA")
