import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

# [[素因数,数]]を出力
def fctr1(n):
    f = []
    c = 0
    r = int(n ** 0.5)
    for i in range(2, r + 2):
        while n % i == 0:
            c += 1
            n = n // i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


f = fctr1(N)

ans = 0
for n, v in f:
    c = 1
    while 0 < v:
        v -= c
        c += 1

        if v >= 0:
            ans += 1

print(ans)
