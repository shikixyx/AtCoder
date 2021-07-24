import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    S = list(input())

    ans = "Takahashi"
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 1:
                ans = "Aoki"

            break

    print(ans)

    return


if __name__ == "__main__":
    main()
