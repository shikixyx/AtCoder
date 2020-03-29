import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)

p_idx = 0
q_idx = 0
r_idx = 0

p = P[p_idx]
q = Q[q_idx]
r = R[r_idx]


ans = 0
while X > 0 or Y > 0:
    #print("X=", X, "Y=", Y)
    #print("p,q,r", p, q, r)
    #print("ans", ans)
    #print("p,q,r,X,Y,ans", p, q, r, X, Y, ans)

    m = max(p, q, r)

    if m == -1:
        break

    if m == r:
        ans += r
        r_idx += 1

        if r_idx == C:
            r = -1
        else:
            r = R[r_idx]

        lp = p_idx + X - 1
        lq = q_idx + Y - 1

        if lp <= A-1 and lq <= B-1:
            p_l = P[lp]
            q_l = Q[lq]

            if q_l <= p_l:
                Y -= 1
            else:
                X -= 1
        elif B-1 < lq:
            Y -= 1
        else:
            X -= 1

    elif m == p:
        ans += p
        p_idx += 1
        X -= 1

        if p_idx == A or X == 0:
            p = -1
        else:
            p = P[p_idx]
    elif m == q:
        ans += q
        q_idx += 1
        Y -= 1

        if q_idx == B or Y == 0:
            q = -1
        else:
            q = Q[q_idx]

print(ans)
