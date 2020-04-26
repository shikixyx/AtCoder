import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())
L = len(S)

c = 0
t = 0
md = [0] * 2019
md[0] += 1
for i in range(L - 1, -1, -1):
    t += int(S[i]) * pow(10, c, 2019)
    c += 1
    md[t % 2019] += 1

ans = 0
for i in range(2019):
    m = md[i]

    if m == 0:
        continue

    ans += m * (m - 1) // 2

print(ans)
