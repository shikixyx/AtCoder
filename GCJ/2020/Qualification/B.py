import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(input())


def makePar(num, isOpen):
    num = abs(num)
    par = '(' if isOpen else ')'
    ret = [par] * num
    return "".join(ret)


def solve(S):
    ret = []
    prev = 0

    S += ['0']

    for s in S:
        d = int(s)
        if d == 0:
            if prev == 0:
                ret.append(d)
            else:
                p = makePar(prev, False)
                ret.append(p)
                ret.append(d)
        else:
            if prev == d:
                ret.append(d)
            else:
                p = makePar(prev - d, d > prev)
                ret.append(p)
                ret.append(d)

        prev = d

    ret = ret[:-1]

    return "".join(map(str, ret))


ans = []
for i in range(1, T + 1):
    r = solve(list(input()))
    txt = "Case #{}: {}".format(i, r)
    ans.append(txt)

print("\n".join(ans))
exit(0)
