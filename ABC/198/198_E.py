import sys
import copy

# from collections import defaultdict

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
    stack = [(1, -1, set())]
    while stack:
        x, parent, cs = stack.pop()
        color = C[x]

        # print(x, color, cs)

        if not color in cs:
            ans.append(x)
            cs.add(color)

        L = len(PATH[x])
        for v in PATH[x]:
            if v == parent:
                continue

            if x == 1:
                if L == 1:
                    stack.append((v, x, cs))
                else:
                    stack.append((v, x, copy.copy(cs)))
            else:
                if L == 2:
                    stack.append((v, x, cs))
                else:
                    stack.append((v, x, copy.copy(cs)))

    ans.sort()
    print("\n".join(map(str, ans)))

    return


if __name__ == "__main__":
    main()
