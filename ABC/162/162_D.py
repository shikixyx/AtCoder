import itertools
import bisect
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
S = list(input())

R = []
G = []
B = []
for i in range(N):
    s = S[i]
    if s == 'R':
        R.append(i)
    elif s == 'G':
        G.append(i)
    elif s == 'B':
        B.append(i)

cnt = 0
for A, B, C in itertools.permutations([('R', R), ('G', G), ('B', B)]):
    a_s, A = A
    b_s, B = B
    c_s, C = C
    LA = len(A)
    LB = len(B)
    LC = len(C)

    A_to_B = [bisect.bisect_right(B, x) for x in A]
    B_to_C = [bisect.bisect_right(C, x) for x in B]

    print(a_s, b_s, c_s, LA, LB, LC)
    print(A_to_B, B_to_C)

    for i in range(LA):
        a2b = A_to_B[i]

        if LB - 1 < a2b:
            continue

        b2c = B_to_C[a2b]

        if LC - 1 < b2c:
            continue

        cnt += (LB - a2b) * (LC - b2c)

        a = A[i]
        for j in range(b2c, LB):
            b = B[j]
            c = b + (b - a)
            if N - 1 < c:
                break
            if S[c] == c_s:
                cnt -= 1


print(cnt)
