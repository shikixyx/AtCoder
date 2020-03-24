import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())


def makeS(len, n, k, res):
    #print(len, n, k, res)
    ans = []
    if len == n:
        return [res]

    for i in range(k + 1):
        s = chr(97+i)
        if i == k:
            l = makeS(len, n + 1, k + 1, res + s)
        else:
            l = makeS(len, n + 1, k, res + s)

        ans += l

    return ans


ans = makeS(N, 0, 0, "")

print("\n".join(ans))
