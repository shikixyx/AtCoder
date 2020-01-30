import sys
sys.setrecursionlimit(10 ** 7)

# 尺取り法
# しゃくとり法

N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

ans = 0
right = 0
sm = 1

for i in range(N):
    if S[i] == 0:
        ans = N
        break

    # 次の積まで取っても良いか？
    while right < N and sm * S[right] <= K:
        sm *= S[right]
        right += 1

    #print("i,right,sm", i, right, sm)

    ans = max(ans, right-i)

    # 追い越さないように注意
    if i == right:
        right += 1
    else:
        sm //= S[i]

print(ans)
