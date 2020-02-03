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

    print("a", a)
    print("DIFF", len(DIFF), DIFF)
    if len(DIFF) > 3:
        return 'No'
    elif len(DIFF) == 0:
        return 'Yes'

    if len(DIFF) == 1:
        d, prev, op = DIFF[0][0], DIFF[0][1], DIFF[0][2]

        if (op == 3 and prev == 2) or (op == 1 and prev == 3):
            return 'Yes'

        if (prev == 1 and op == 2):
            return 'Yes'

        return 'No'

    if len(DIFF) == 2:
        d1, p1, op1 = DIFF[0][0], DIFF[0][1], DIFF[0][2]
        d2, p2, op2 = DIFF[1][0], DIFF[1][1], DIFF[1][2]

        if d2 - d1 == 1:
            if p1 == 1 and op1 == 3 and op2 == 2:
                if a[d1 - 1] - a[d2] != 1:
                    return 'Yes'
            if p1 == 2 and op2 == 2:
                if a[d1 - 1] - a[d2] >= 2:
                    return 'Yes'
            return 'No'

        if d1 == 0:
            if op1 == 1 and (p2 == 1 and op2 == 2):
                if a[d1] != 0:
                    return 'Yes'
                return 'No'
            if (p1 == 1 and op1 == 2) and p2 == 2:
                if a[d2 - 1] != 0:
                    return 'Yes'
                return 'No'
            return 'No'

    if len(DIFF) == 3:
        d1, p1, op1 = DIFF[0][0], DIFF[0][1], DIFF[0][2]
        d2, p2, op2 = DIFF[1][0], DIFF[1][1], DIFF[1][2]
        d3, p3, op3 = DIFF[2][0], DIFF[2][1], DIFF[2][2]

        if d3 - d2 == 1 and d2 - d1 == 1:
            if p1 == 1 and op1 == 2 and op3 == 2:
                if a[d1] - a[d3] >= 2:
                    return 'Yes'

        return 'No'

    return 'No'


ans = []
for i in range(T):
    n, a = A[i][0], A[i][1]
    r = can_sharpening(n, a)
    ans.append(r)

print("\n".join(ans))
