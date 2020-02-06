
# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 最小値
minimum = 10 ** 18

# 配列の要素aで１つずつ
for a in A:
    # aが何回２で割れたかを入れる変数
    c = 0

    # aが２で割れる間
    while a % 2 == 0:
        # aを２でわる
        a //= 2
        c += 1

    # もし、minimumよりもcが小さかったら
    if minimum > c:
        minimum = c
    # minimumを更新

print(minimum)
