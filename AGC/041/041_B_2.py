import sys
from collections import defaultdict
from collections import deque

'''
Second Try
Not Accept
'''

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M, V, P = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

#NUM = [0] * N
#ACN = [0] * N
NUM = defaultdict(int)
ACN = defaultdict(int)
cnt = 0
mx = A[0]

# cnt and accumulation
for a in A:
    d = mx - a
    cnt += 1
    NUM[d] += 1
    ACN[d] = cnt

print(NUM)

# P Number Problem
PROBLEM_P = 0
p = P
for i in range(0, A[0]+1):
    if NUM[i] == 0:
        continue

    p -= NUM[i]

    if p < 0:
        PROBLEM_P = i
        break

    if i == (A[0]+1) and p > 0:
        print(N)
        exit()

#print("NUM", NUM)
#print("PROBLEM_P", PROBLEM_P)

# R Number Problem
R = PROBLEM_P + M

# P-1 Problem
ans = 0
NG_POINT = (P-1) * M
NG_POINT += (N - ACN[R]) * M
MV = M * V

# p problem num
num_p = ACN[PROBLEM_P] - P

for r in range(R, -1, -1):
    need_point = M
    total = (need_point * NUM[r]) + NG_POINT

    for q in range(r-1, PROBLEM_P, -1):
        if NUM[q] == 0:
            continue
        total += NUM[q] * (q - r + M)

    total += num_p * (PROBLEM_P - r + M)

    if total >= MV:
        ans = r
        break
    else:
        NG_POINT += NUM[r] * M

print(ACN[ans])
