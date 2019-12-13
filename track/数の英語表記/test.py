num_to_eng = {
      1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
      6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
      11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
      16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
      30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
      80: 'eighty', 90: 'ninety'
    }

for i in range(20, 100):
  if i % 10 != 0:
    first_digit = int(str(i)[-1])
    ten_digit = int(str(i)[0]) * 10
    num_to_eng[i] = num_to_eng[ten_digit] + ' ' + num_to_eng[first_digit]

for i in range(10**2, 10**3):
    if i % 100 == 0:
        hundred_digit = int(str(i)[0])
        num_to_eng[i] = num_to_eng[hundred_digit] + ' ' + 'hundred'
    else:
        ten_digit = int(str(i)[1:])
        hundred_digit = int(str(i)[0]) * 100
        num_to_eng[i] = num_to_eng[hundred_digit] + ' ' + num_to_eng[ten_digit]

for i in range(10**3, 10**6):
    if i % 10**3 == 0:
        a = i / 10**3
        thousand_digit = int(str(i)[0]) * a
        num_to_eng[i] = num_to_eng[thousand_digit] + ' ' + 'thousand'
    else:
        if i > 10**4:
            hundred_digit = int(str(i)[2:])
            thousand_digit = int(str(i)[:2]) * 10**3
        else:
            hundred_digit = int(str(i)[1:])
            thousand_digit = int(str(i)[:1]) * 10**3
        num_to_eng[i] = num_to_eng[thousand_digit] + ' ' + num_to_eng[hundred_digit]


print(num_to_eng[10**5])
