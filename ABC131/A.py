s = input()
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        print('Bad')
        break
else:
    print('Good')
