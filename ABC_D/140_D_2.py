import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 90min
# 解答見た
# コーナーケース
# むずい

N, K = map(int, input().split())
S = list(input())

START = S[0]
prev = S[0]
ans = 0
for i in range(1, N):
    s = S[i]

    # 一緒だったら+1
    if prev == s:
        ans += 1

    # 最後の時だけ場合わけ
    if i == N - 1:
        if s == START and K > 0:
            if prev != s:
                ans += 2
        else:
            if K > 0:
                ans += 1

    # 最後以外
    else:
        # 前と異なる
        if prev != s:
            if s == START and K > 0:
                ans += 2
                K -= 1

            prev = s


print(ans)
