import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)

# Not AC


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [a << 1 for a in A]
B = [b << 1 for b in B]

cntA = [[0] * 4 for _ in range(29)]
cntB = [[0] * 4 for _ in range(29)]


print(A)
print(B)

for a in A:
    i = 0
    while a > 0:
        bit = a & 3
        cntA[i][bit] += 1
        a >>= 1
        i += 1

for b in B:
    i = 0
    while b > 0:
        bit = b & 3
        cntB[i][bit] += 1
        b >>= 1
        i += 1

print(cntA)
print(cntB)

ans = 0
for i in range(29):
    one = 0
    one += cntA[i][0] * (cntB[i][2] + cntB[i][3])
    one += cntA[i][1] * (cntB[i][1] + cntB[i][2])
    one += cntA[i][2] * (cntB[i][0] + cntB[i][1])
    one += cntA[i][3] * (cntB[i][0] + cntB[i][3])
    print("i,one", i, one)
    bit = one % 2
    ans += 2 ** i * bit

print(ans)
