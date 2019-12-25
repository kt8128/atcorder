import sys

def main():
    h, a, b = map(int, input().split())
    if h <= a:
      print("YES")
      print(1)
      exit()
    elif a <= b:
      print('NO')
      exit()
    else:
        print("YES")
        if h % (a-b) == 0:
          print(h//(a-b)-1)
        elif h % (a-b) <= b:
          print(h//(a-b))
        else:
          print(h//(a-b)-1)

    count = 0
    while h > 0:
      h -= a
      if h <= 0:
        count += 1
        break
      h += b
      count += 1
    print("YES")
    print(idx)


if __name__ == '__main__':
    main()
