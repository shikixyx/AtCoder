import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
W.sort()

NH = [0] + H + [10 ** 9 + 10]

even_diff = []
odd_diff = []
d = 0
for i in range(0, N, 2):
    d += NH[i + 1] - NH[i]
    even_diff.append(d)

d = 0
for i in range(1, N + 1, 2):
    d += NH[i + 1] - NH[i]
    odd_diff.append(d)

ans = float("inf")
idx = 0

# 最初に追加する場合
while idx < M and W[idx] < H[0]:
    diff = even_diff[N // 2] - W[idx]
    ans = min(ans, diff)
    idx += 1

if idx == M:
    print(ans)
    exit()

# print("odd_diff", odd_diff)
# print("even_diff", even_diff)

# 間に追加する場合
for i in range(N - 1):
    while idx < M and H[i] <= W[idx] < H[i + 1]:
        diff = 0

        # 奇数の方にペア
        odd = i if i % 2 == 1 else i + 1
        even = i if i % 2 == 0 else i + 1

        # ここまでのやつ
        if even != 0:
            diff += odd_diff[even // 2 - 1]

        # ここからのやつ
        diff += even_diff[N // 2] - even_diff[even // 2]

        # 今回の分
        diff += abs(W[idx] - H[even])

        # 更新
        # print(idx, H[i], H[i + 1], W[idx], diff)
        ans = min(ans, diff)

        idx += 1

if idx == M:
    print(ans)
    exit()

# 最後に追加
diff = odd_diff[N // 2] - (10 ** 9 + 10 - W[idx])
ans = min(diff, ans)

print(ans)

