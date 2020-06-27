import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

ANS = []
c = 26
p = 97

while True:
    N -= 1
    n = N % 26
    ANS.append(chr(p + n))

    if N < 26:
        break

    N -= n
    N //= 26


print("".join(map(str, ANS[::-1])))

