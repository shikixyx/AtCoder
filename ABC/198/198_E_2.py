import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    C = [-1] + list(map(int, input().split()))

    PATH = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B = list(map(int, input().split()))
        PATH[A].append(B)
        PATH[B].append(A)

    ans = []
    stack = [(1, -1, defaultdict(lambda: False))]
    while stack:
        x, parent, cs = stack.pop()
        color = C[x]

        # print(x, color, cs)

        if not cs[color]:
            ans.append(x)
            cs[color] = True

        for v in PATH[x]:
            if v == parent:
                continue
            stack.append((v, x, cs.copy()))

    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
