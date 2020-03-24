import numpy as np
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 30min
# N + N/2 + N/3 + .... + N/N = O(logN) は覚えておこう
# 積分との比較から導出

N = int(input())
A = list(map(int, input().split()))

half = N // 2

ball = np.zeros(N, dtype=np.bool)
ball[half:] = A[half:]

for i in range(half - 1, -1, -1):
    a = A[i]
    cnt = np.count_nonzero(ball[i:: i + 1]) % 2
    if a != cnt:
        ball[i] = True

ans = np.where(ball == True)[0]
print(len(ans))

if len(ans) > 0:
    print(" ".join([str(x+1) for x in ans]))
