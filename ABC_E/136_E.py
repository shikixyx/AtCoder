import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 回答見た
# Pypy3

N, K = map(int, input().split())
A = list(map(int, input().split()))


S = sum(A)
divisors = []

for i in range(1, S):
    if S < i * i:
        break

    if S % i == 0:
        divisors.append(i)
        divisors.append(S // i)


def check(x):
    modX = [a % x for a in A if a % x != 0]
    modX.sort()

    L = len(modX)
    rtn = False

    for i in range(L):
        cnt = 0
        minus = modX[:i]
        plus = modX[i:]

        cnt_minus = sum(minus)
        cnt_plus = x * (L - i) - sum(plus)

        if cnt_minus <= K and cnt_plus <= K:
            rest = abs(cnt_minus - cnt_plus)
            if rest % x == 0:
                rtn = True
                break

    return rtn


ans = 1
for x in divisors:
    if check(x):
        ans = max(x, ans)

print(ans)
