import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    AB.sort()

    prev = 0
    ans = 0
    for a, b in AB:
        if a <= K:
            K += b

    print(min(pow(10, 100), K))

    return


if __name__ == "__main__":
    main()
