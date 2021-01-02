import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    T = []
    P = 0
    for a, b in AB:
        P += a
        T += [a + a + b]

    T.sort(reverse=True)
    d = 0
    ans = 1
    for i in range(N):
        d += T[i]
        if d > P:
            ans += i
            break

    print(ans)

    return


if __name__ == "__main__":
    main()
