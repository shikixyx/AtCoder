import sys
sys.setrecursionlimit(10 ** 7)

A = []
for _ in range(3):
    a = list(map(int, input().split()))
    A += a

N = int(input())

OPEN = []
for _ in range(N):
    b = int(input())

    if b in A:
        OPEN.append(A.index(b))

#print(OPEN)

ans = 'No'

if 0 in OPEN:
    if 1 in OPEN and 2 in OPEN:
        print('Yes')
        exit()

    if 3 in OPEN and 6 in OPEN:
        print('Yes')
        exit()

    if 4 in OPEN and 8 in OPEN:
        print('Yes')
        exit()

if 1 in OPEN:
    if 4 in OPEN and 7 in OPEN:
        print('Yes')
        exit()

if 2 in OPEN:
    if 5 in OPEN and 8 in OPEN:
        print('Yes')
        exit()

    if 4 in OPEN and 6 in OPEN:
        print('Yes')
        exit()

if 3 in OPEN:
    if 4 in OPEN and 5 in OPEN:
        print('Yes')
        exit()

if 6 in OPEN:
    if 7 in OPEN and 8 in OPEN:
        print('Yes')
        exit()

print('No')
exit()
