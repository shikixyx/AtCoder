import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())
A = []
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    A.append((n, a))


# "<" 1
# ">" 2
# "=" 3
def can_sharpening(n, a):
    DIFF = []
    prev = -1
    SWAP = []
    cnt = 0
    for i in range(1, n):
        if a[i - 1] < a[i]:
            op = 1
        elif a[i - 1] > a[i]:
            op = 2
        else:
            op = 3

        if prev != -1 and prev != op:
            DIFF.append((i, prev, op))

        prev = op


ans = []
for i in range(T):
    n, a = A[i][0], A[i][1]
    r = can_sharpening(n, a)
    ans.append(r)

print("\n".join(ans))
