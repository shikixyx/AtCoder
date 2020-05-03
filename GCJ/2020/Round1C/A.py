import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    X, Y, M = readline().split()
    X = int(X)
    Y = int(Y)
    M = M.decode(encoding="utf-8")

    ans = 0
    if X == 0 and Y == 0:
        return 0

    ok = False
    for s in M:
        ans += 1
        if s == "N":
            Y += 1
        elif s == "S":
            Y -= 1
        elif s == "E":
            X += 1
        elif s == "W":
            X -= 1

        print(X, Y)
        if abs(X) + abs(Y) <= ans:
            ok = True
            break

    if not ok:
        ans = "IMPOSSIBLE"

    return ans


ans = []
for i in range(1, T + 1):
    t = solve()
    txt = "Case #{}: {}".format(i, str(t))
    ans.append(txt)

print("\n".join(ans))
