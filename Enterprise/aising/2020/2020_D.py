import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
X = list(input())

pc = X.count("1")

# X == 0 の時
if pc == 0:
    for i in range(N):
        print(1)
    exit()

sml = pc - 1
big = pc + 1

b = 0
mod_s = 0
mod_b = 0
for x in X[::-1]:
    if x == "1":
        if sml:
            mod_s += pow(2, b, sml)
            mod_s %= sml

        mod_b += pow(2, b, big)
        mod_b %= big

    b += 1


ELE = []

b = 0
for x in X[::-1]:
    if x == "0":
        t = (mod_b + pow(2, b, big)) % big
        ELE.append((t, 1))
    else:
        t = (mod_s - pow(2, b, sml)) % sml if sml else 0

        if sml:
            ELE.append((t, 1))
        else:
            ELE.append((0, 0))
    b += 1


def solve(x, c):
    if x == 0:
        return c

    b = 0
    nx = x
    while nx > 0:
        b += nx & 1
        nx >>= 1

    ret = solve(x % b, c + 1)
    return ret


ANS = []
for x, pc in ELE:
    ANS.append(solve(x, pc))

print("\n".join(map(str, ANS[::-1])))

