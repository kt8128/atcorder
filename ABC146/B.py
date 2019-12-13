def rot13(c, n):
    if 'A' <= c and c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + n) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + n) % 26 + ord('a'))

    # その他の文字は対象外
    return c


n = int(input())
s = input()
ans = []

for i in list(s):
    ans.append(rot13(i, n))

print(''.join(ans))
