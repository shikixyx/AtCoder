import sys
import itertools
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


A = list(input())
B = list(input())
C = list(input())


def compare(arr1, arr2):
    for x, y in zip(arr1, arr2):
        if x == y or x == '?' or y == '?':
            continue
        return False

    return True


def can_match(x, y):
    return x == '?' or y == '?' or x == y


CONST = 2005
ans = len(A) + len(B) + len(C)


for A, B, C in itertools.permutations([A, B, C]):

    A_to_B = [True] * CONST
    B_to_C = [True] * CONST
    A_to_C = [True] * (CONST * 2)

    lenA = len(A)
    lenB = len(B)
    lenC = len(C)

    for i in range(lenA+1):
        A_to_B[i] = compare(A[i:], B)

    for i in range(lenB + 1):
        B_to_C[i] = compare(B[i:], C)

    for i in range(lenA+1):
        A_to_C[i] = compare(A[i:], C)

    for i in range(CONST):
        for j in range(CONST):
            if A_to_B[i] and B_to_C[j] and A_to_C[i + j]:
                right = max(lenA, i + lenB, i + j + lenC)
                ans = min(ans, right)

print(ans)
