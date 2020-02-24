import sys

sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))


ans = True
for a in A:
    if a % 2 == 0:
        if not (a % 5 == 0 or a % 3 == 0):
            ans = False
            break


if ans:
    print('APPROVED')
else:
    print('DENIED')
