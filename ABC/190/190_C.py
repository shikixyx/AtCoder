import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    K = int(input())
    CD = [list(map(int, input().split())) for _ in range(K)]

    ans = 0
    for i in range(2 ** K):
        BALL = [False] * (N + 1)
        for j in range(K):
            if i & 1:
                BALL[CD[j][0]] = True
            else:
                BALL[CD[j][1]] = True

            i >>= 1

        t = 0
        for a, b in AB:
            if BALL[a] and BALL[b]:
                t += 1

        ans = max(t, ans)

    print(ans)

    return


if __name__ == "__main__":
    main()
