import sys
import requests


def main():
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    inp = input()
    api_url = 'http://challenge-server.code-check.io/api/hash'
    params = {'q': inp}
    res = requests.get(api_url, params).json()
    print(res)

if __name__ == '__main__':
    main()
