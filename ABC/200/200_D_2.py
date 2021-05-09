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

        DP[i + 1] = DP[i][:]

        ## 1つだけ使う
        if DP[i + 1][a]:
            B = [i]
            C = DP[i + 1][a]
            break
        else:
            DP[i + 1][a] = [i]

        for j in range(200):
            if DP[i][j]:
                ## 今回のを加えたやつ
                t = DP[i][j][:]
                t.append(i)

                if DP[i + 1][(a + j) % 200]:
                    B = t
                    C = DP[i + 1][(a + j) % 200]
                    break
                else:
                    DP[i + 1][(a + j) % 200] = t

        if B:
            break

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
