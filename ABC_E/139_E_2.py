import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# O(N^2)


N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

A = [[-1]] + A


def check(a, q=[]):
    if not A[a]:
        return False

    b = A[a][-1]
    b_op = A[b][-1]

    ok = False
    if a == b_op:
        ok = True

        if b < a:
            a, b = b, a
        q.append((a, b))

    return ok


q = []
for i in range(1, N + 1):
    check(i, q)

q = list(set(q))

day = 0
while q:
    nq = []
    for a, b in q:
        A[a].pop()
        A[b].pop()
        check(a, nq)
        check(b, nq)

    day += 1
    q = list(set(nq))

for i in range(1, N + 1):
    if len(A[i]) != 0:
        print(-1)
        exit()

print(day)
exit()
