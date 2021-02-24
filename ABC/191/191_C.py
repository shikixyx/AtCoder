import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    H, W = map(int, input().split())
    S = [["."] * (W + 1)]
    for _ in range(H):
        s = ["."] + list(input()) + ["."]
        S.append(s)
    S.append([["."] * (W + 1)])

    print(S)

    ans = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                continue

            if S[i - 1][j] == "." and S[i - 1][j - 1] == "." and S[i][j - 1] == ".":
                ans.add((i, j, 1))

            if S[i - 1][j] == "." and S[i - 1][j + 1] == "." and S[i][j + 1] == ".":
                ans.add((i, j, 2))

    return


if __name__ == "__main__":
    main()
