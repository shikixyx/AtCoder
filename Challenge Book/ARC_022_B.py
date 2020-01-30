from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 7)

# 尺取り法
# しゃくとり法

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
right = 0
ans = 0
for i in range(N):
    while right < N and cnt[A[right]] == 0:
        cnt[A[right]] += 1
        right += 1

    #print("i,right", i, right)
    ans = max(right - i, ans)

    if right == i:
        right += 1
    else:
        cnt[A[i]] = 0

print(ans)
