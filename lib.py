# mergeソート、マージソート
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


# 素数判定
def is_prime(q):
    q = abs(q)
    if q == 2:
        return True
    if q < 2 or q & 1 == 0:
        return False
    return pow(2, q-1, q) == 1
