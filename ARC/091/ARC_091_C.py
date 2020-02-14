import sys
sys.setrecursionlimit(10 ** 7)

NM = [int(x) for x in input().split()]
NM.sort()
N = NM[0]
M = NM[1]

if N == 1:
    if M >= 3:
        ans = M - 2
    elif M == 1:
        ans = 1
    else:
        ans = 0

    print(ans)
    exit()
elif N == 2:
    print(0)
    exit()

ans = (N - 2) * (M - 2)

print(ans)
