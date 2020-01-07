import sys
from collections import defaultdict
from collections import deque

'''
Third Try
Accept
'''


read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


N, M, V, P = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

# A_P -> A_X (A_P - M = A_X)
A_P = A[P-1]
A_X = A[P]
i_X = P
for i in range(P, len(A)):
    if (A_P - A[i]) > M:
        A_X = A[i-1]
        i_X = i-1
        break
    elif i == (len(A)-1):
        A_X = A[i]
        i_X = i
    else:
        continue

NG_POINT = (P-1) * M


def isPossible(i):
    if (i+1) < P:
        return True
    elif i > i_X:
        return False

    MV = M * V
    ax = A[i]
    score = ax + M

    total = M + NG_POINT
    total += (N - i - 1) * M

    for j in range(i-1, P-2, -1):
        total += score - A[j]

    #print("i", i, "total", total, "NG_POINT", NG_POINT)

    if total >= MV:
        return True

    return False


left = 0
right = i_X

if not isPossible(left):
    print(1)
    exit()

if isPossible(i_X):
    print(i_X + 1)
    exit()

#print("A", A, "i_X", i_X)

for _ in range(i_X):
    #print("left", left, isPossible(left), "right", right, isPossible(right))
    if (left + 1) == right:
        break

    mid = (left + right) // 2

    if isPossible(mid):
        left = mid
    else:
        right = mid

print(left + 1)
