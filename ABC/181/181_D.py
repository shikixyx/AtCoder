import sys
from collections import Counter
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = list(input())
eight = [x for x in range(100, 1000) if x % 8 == 0]
C = Counter(S)

if len(S) < 3:
    ans = False
    for x in itertools.permutations(S):
        x = int("".join(x))
        if x % 8 == 0:
            print("Yes")
            ans = True
            break

    if not ans:
        print("No")

    exit()


ans = False
num = 0

for x in eight:
    flg = True
    XC = Counter(str(x))

    if XC["0"] > 0:
        continue

    for i in range(1, 10):
        if C[str(i)] >= XC[str(i)]:
            continue
        else:
            flg = False
            break

    if flg:
        ans = True
        num = str(x)
        break

if not ans:
    print("No")
else:
    print("Yes")
    exit()
    ans = []
    for i in range(1, 10):
        c = C[str(i)] - XC[str(i)]
        if c > 0:
            ans += [i] * c

    ans += [num]

    print("".join(map(str, ans)))

