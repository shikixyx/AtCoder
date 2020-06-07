import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = list(input())

    while S[-1] == "1" and A[-1] == 0:
        S.pop()
        A.pop()
        N -= 1

    if N == 0:
        return 0

    if S[-1] == "1":
        return 1

    candidate = [set([0]) for _ in range(2)]

    # 1より下の0で作れるか?
    OK = True
    for i in range(N)[::-1]:
        a = A[i]
        s = int(S[i])

        nxt = []
        for x in list(candidate[0]):
            nxt.append(x)
            nxt.append(x ^ a)

        candidate[s] = set(nxt)

        if s == 1:
            zero = candidate[0]
            one = candidate[1]

            if one <= zero:
                pass
            else:
                OK = False
                break

    ans = 1

    if OK:
        ans = 0

    return ans


ANS = []
for _ in range(T):
    t = solve()
    ANS.append(t)

print("\n".join(map(str, ANS)))
