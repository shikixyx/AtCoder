import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    DP = [[False] * 200 for _ in range(210)]
    B = []
    C = []

    for i in range(N):
        a = A[i]

        for j in range(200):
            if j == 0:
                if DP[i][a]:
                    B = [i]
                    C = DP[i][a]
                    break

                DP[i + 1][a] = [i]
            else:
                if not DP[i][j]:
                    continue

                t = DP[i][j][:]
                t.append(i)

                if DP[i + 1][(a + j) % 200]:
                    B = t
                    C = DP[i + 1][(a + j) % 200]
                    break

                DP[i + 1][(a + j) % 200] = t
                DP[i + 1][j] = DP[i][j]

    if B:
        B = [b + 1 for b in B]
        C = [c + 1 for c in C]
        B = [len(B)] + B
        C = [len(C)] + C

        print("Yes")
        print(" ".join(map(str, B)))
        print(" ".join(map(str, C)))
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
