import sys
sys.setrecursionlimit(10 ** 7)

T = int(input())
A = []
for _ in range(T * 2):
    a = int(input())
    A.append(a)


def digit_sum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)


def make_enbe(n, x):
    sm = digit_sum(x)
    sx = str(x)
    if (sm % 2 == 0) and int(sx[n - 1]) % 2 == 1:
        return x

    # delte last num
    d = 0
    for i in range(1, n + 1):
        if int(sx[-i]) % 2 == 0:
            continue
        else:
            d = i
            break

    if d == 0:
        return - 1

    sx = sx[:-d+1] if d != 1 else sx

    sm = digit_sum(sx)
    if sm % 2 == 0:
        return int(sx)
    elif len(sx) == 1:
        return -1

    d = 0
    for i in range(2, len(sx) + 1):
        if int(sx[-i]) % 2 == 1:
            d = i
            break

    if d == 0:
        return - 1
    else:
        r = int(sx[0:-d] + sx[-d + 1:])
    return r


ans = []
for i in range(T):
    n, x = A[i * 2], A[i * 2 + 1]
    a = make_enbe(n, x)
    ans.append(str(a))

print("\n".join(ans))
