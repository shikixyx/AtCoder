import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M, T = map(int, input().split())

    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.append([T, 10 ** 10])

    prev = 0
    flg = True
    B = N
    for a, b in AB:
        N -= a - prev
        if N <= 0:
            flg = False
            break

        N += b - a
        N = min(N, B)
        prev = b

    if flg:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
