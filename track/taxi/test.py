import math

def main():
  a, b, c, d = map(int, input().split())
  n = int(input())
  ans = 0
  for _ in range(n):
      t, l = input().split()
      l = int(l)
      t = int(t.split(':')[0])
      if t >= 22:
          e = 1.2
      else:
          e = 1.0
      ans += math.floor((b + d*math.ceil(max(0, l-a)/c)) * e)
  print(ans)

if __name__ == '__main__':
    main()
