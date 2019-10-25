import sys
import pandas as pd
import math

args = sys.argv

d, d_prime = int(args[1]), int(args[2])
x, x_prime, y, y_prime, q = 1, 0, 0, 1, 0

df = pd.DataFrame([[d, d_prime, x, x_prime, y, y_prime, q]], columns=["d", "d_prime", "x", "x_prime", "y", "y_prime", "q"])

while d_prime != 0:
    d_prev, d_prime_prev, x_prev, x_prime_prev, y_prev, y_prime_prev = d, d_prime, x, x_prime, y, y_prime
    q = math.floor(d_prev / d_prime_prev)
    d, d_prime = d_prime_prev, d_prev-q*d_prime_prev
    x, x_prime, y, y_prime = x_prime_prev, x_prev-q*x_prime_prev, y_prime_prev, y_prev-q*y_prime_prev
    df1 = pd.DataFrame([[d, d_prime, x, x_prime, y, y_prime, q]], columns=df.columns)
    df = df.append(df1)

print(df)
