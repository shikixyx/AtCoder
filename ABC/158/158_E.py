import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, P = map(int, input().split())
S = list(map(int, list(input())))
# print(S)
S.reverse()

ans = 0
if P == 2 or P == 5:
    cnt = 0
    for i in range(N):
        if S[i] % P == 0:
            ans += N - i

else:
    cummod = [0] * P

    d = 1
    prev = 0
    for i in range(N):
        m = (S[i] * d) % P
        m += prev
        m %= P
        cummod[m] += 1
        d *= 10
        d %= P
        prev = m

    #cummod[0] += 1

    for n in cummod:
        if n <= 1:
            continue
        ans += n * (n - 1) // 2

    ans += cummod[0]

print(ans)
