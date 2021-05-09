import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    cnt = [0] * 200
    for a in A:
        cnt[a % 200] += 1

    for i in range(200):
        c = cnt[i]
        if c == 0:
            continue
        ans += (c * (c - 1)) // 2

    print(ans)

    return


if __name__ == "__main__":
    main()
