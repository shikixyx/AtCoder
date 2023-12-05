# 問題
# 1. 以下の条件を満たす関数fを実装してください
#     - fは引数を2つ受け取ります
#         - 1つ目の引数は整数型のseedです
#         - 2つ目の引数は整数型のnです
#     - fは以下の条件を満たす整数を返します
#         - 2つ目の引数が0の場合、1を返す
#         - 2つ目の引数が2の場合、2を返す
#         - 2つ目の引数が偶数の場合、以下の式を返す
#             - f(seed, n-1) + f(seed, n-2) + f(seed, n-3) + f(seed, n-4)
#         - 2つ目の引数が奇数の場合、以下のAPIを呼び出し、その結果を返す
#             - URL: http://challenge-server.code-check.io/api/recursive/ask?seed={seed}&n={n}
#             - {seed}は1つ目の引数の値で置き換える
#             - {n}は2つ目の引数の値で置き換える
#             - APIのレスポンスは以下の形式で返ってくる
#                 - {"result": {整数}}
#                 - {整数}の部分を整数型に変換して返す
# 2. f(seed, n)を計算して出力してください
#     - seedはコマンドライン引数の1つ目の引数です
#     - nはコマンドライン引数の2つ目の引数です


import sys
import requests
from functools import lru_cache

URL = "http://challenge-server.code-check.io/api/recursive/ask?seed={}&n={}"

def main(argv):
    # return if args is not two
    if len(argv) != 2:
        print("Please input two args.")
        exit(1)
    
    # capture and validate
    try:
        seed = argv[0]
        n = int(argv[1])
    except ValueError:
        print("Please input integer.")
        exit(1)
    
    print(f(seed,n))
    return
    
    
@lru_cache(maxsize=None)
def f(seed,n):
    if n == 0:
        return 1
    if n == 2:
        return 2

    if n % 2 == 0:
        return f(seed,n-1) + f(seed,n-2) + f(seed,n-3) + f(seed,n-4)
    else:
        return ask_server(seed,n)

def ask_server(seed,n):
    response = requests.get(URL.format(seed, n))

    # if response is not 200, exit with 1
    if response.status_code != 200:
        print("Error: status code is not 200.")
        exit(1)
    
    # parse json and return result if it is integer
    result = response.json()["result"]
    if type(result) is not int:
        print("Error: result is not integer.")
        exit(1)
    
    return result


if __name__ == '__main__':
    main(sys.argv[1:])
