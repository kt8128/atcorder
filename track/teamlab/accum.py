import requests
import time
import random
import csv
from collections import defaultdict
import numpy as np

def req(text):
    api_url = 'https://runner.team-lab.com/q'
    token = 'F2g6RyojqAc5LVmdxjdDmd5ZGn6AxvJf'
    params = {'str': text, 'token': token}
    res = requests.get(api_url, params).json()
    return res

def csv_r():
    m = 0
    text = ''
    with open('test.csv', 'r') as f:
        reader = csv.reader(f)
        r = list(reader)
        r = sorted(r, key=lambda x: int(x[1]), reverse=True)
    return r

def main():
    chars = ['A', 'B', 'C', 'D']
    decode = defaultdict(int)
    text = ''
    # res = req(text)
    # with open('test.csv', 'a') as f:
    #     writer = csv.writer(f, lineterminator='\n') # 行末は改行
    #     writer.writerow([text, res])
    l = csv_r()
    for i in range(6):
        text += l[i][0]
    text += "DD"
    res = req(text)
    print(text, res)
    print(decode)

    time.sleep(1)

def accum():
    chars = ['A', 'B', 'C', 'D']
    decode = defaultdict(int)
    text = ''
    for i in range(8):
        text += random.choice(chars)
    res = req(text)
    with open('test.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') # 行末は改行
        writer.writerow([text, res])
    print(text, res)
    print(decode)

    time.sleep(1)
    # ACDDDCAA
    # ACDAABBA

if __name__ == '__main__':
    for i in range(10000):
        accum()
        if i % 50 == 0:
            main()
