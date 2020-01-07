import sys
from collections import defaultdict
from collections import deque

'''
First Try
Not Accept
'''

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M, V, P = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

NUM = [0] * N
ACN = [0] * N
cnt = 0
mx = A[0]


for a in A:
    d = mx - a
    cnt += 1
    NUM[d] += 1
    ACN[d] = cnt

# calc p
p = P
for i in range(0, A[0]):

    if NUM[i] == 0:
        continue

    p -= NUM[i]

    if p < 0:
        p = i
        break

if p < 0:
    print(N)
    exit()

#print("p", p)
#print("NUM", NUM)


R = p + M
if R < 0:
    R = A[0] - A[len(A)-1]

ans = R
NG = N - ACN[R]
PNG = (N - ACN[R]) * M
m = M

#print("R", R)

'''
# PNG
for i in range(R+1, A[N-1]):
    if NUM[i] == 0:
        continue

    if M < (i-R):
        PNG += (N - ACN[i-1]) * M
        break

    PNG += NUM[i] * (i-R)
    NG_notall[(i-R)] = NUM[i]
'''

# loop
for r in range(R, -1, -1):
    m = M
    t = NUM[r]

    if t == 0:
        continue

    sm = M * V

    #print("r", r, "sm", sm, "PNG", PNG, "NUM", NUM[r])

    sm -= (r - p)*NUM[r]
    sm -= PNG
    m -= (r - p)

    if sm < 0:
        ans = r
        break

    rn = r
    for q in range(r-1, -1, -1):
        tq = NUM[q]
        if tq == 0:
            continue

        #t += tq

        if q < p:
            m -= (rn - q)

        if m < 0:
            PNG += NUM[r] * M
            break

        sm -= (rn - q) * t

        #print("q", q, "m", m, "sm", sm, "rn-q", (rn-q), "t", t)

        rn = q
        t += tq

        if sm < 0:
            ans = r
            break

    if sm < 0:
        ans = r
        break

    #print("sm", sm, "m", m)

    if m < 0:
        continue

    pr = p
    for j in range(len(NUM)):
        if NUM[j] == 0:
            continue

        pr -= NUM[j]
        sm -= NUM[j] * (M - j)

        if pr < 0:
            break

    if sm < 0:
        ans = r
        break
    else:
        PNG += NUM[r] * M


# print(ans)
print(ACN[r])
