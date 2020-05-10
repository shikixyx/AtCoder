import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# WA

N = int(input())

left = 0
right = 0

has_z_left = False
has_z_right = False
has_sep = False
ZERO = 0

for _ in range(N):
    S = list(input())
    L = len(S)

    r = 0
    l = 0
    for i in range(L):
        s = S[i]

        if s == ")":
            if l == 0:
                r += 1
            else:
                l -= 1
        elif s == "(":
            l += 1

    R = r

    r = 0
    l = 0
    for i in range(L - 1, -1, -1):
        s = S[i]

        if s == "(":
            if r == 0:
                l += 1
            else:
                r -= 1
        elif s == ")":
            r += 1

    L = l

    if L == 0 and R > 0:
        has_z_left = True

    if R == 0 and L > 0:
        has_z_right = True

    if L == 0 and R == 0:
        ZERO += 1

    if not (L == R and L == 0):
        has_sep = True

    left += L
    right += R


if left == right:
    if not has_sep:
        print("Yes")
    else:
        if (has_z_left and has_z_right) or 2 <= ZERO:
            print("Yes")
        else:
            print("No")
else:
    print("No")
