import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

N, K = map(int, input().split())
S = list(input())

NUM_L = [0] * (N + 1)
NUM_R = [0] * (N + 1)

S += ['M']
prev = 'M'
cnt = 0

for i in range(N+1):
    s = S[i]
    if prev == s and not (i == 0 or i == N):
        cnt += 1

    if not (prev == s):
        if prev == 'L':
            NUM_L[cnt+1] += 1
        elif prev == 'R':
            NUM_R[cnt+1] += 1

        cnt = 0
        prev = s


def check(s):
    ans = 0
    if s == 'L':
        arr1 = NUM_L
        arr2 = NUM_R
    else:
        arr1 = NUM_R
        arr2 = NUM_L

    for i in range(1, N + 1):
        n = arr1[i]
        ans += (i - 1) * n

    cnt = K
    for i in range(N, -1, -1):
        n = arr2[i]
        if n == 0:
            continue

        p = min(cnt, n)

        ans += (i + 1) * p
        cnt -= p

        if cnt == 0:
            break

    return ans


ans = max(check('L'), check('R'))
ans = min(ans, N-1)
print(ans)
