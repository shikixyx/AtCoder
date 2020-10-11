import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10 ** 9 + 7

T = int(input())


def solve():
    N, A, B = map(int, input().split())

    if N < A + B:
        return 0

    # 全部では
    TOTAL = ((N - A + 1) ** 2) % MOD
    TOTAL *= (N - B + 1) ** 2
    TOTAL %= MOD

    # 両方重なっている時を除く

    return


ANS = []
for _ in range(T):
    x = solve()
    ANS.append(x)

print("\n".join(map(str, ANS)))

