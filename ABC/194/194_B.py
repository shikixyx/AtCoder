import sys
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 ** 10
    for i, j in itertools.product(range(N), repeat=2):
        if i == j:
            t = AB[i][0] + AB[j][1]
        else:
            t = max(AB[i][0], AB[j][1])
        ans = min(ans, t)

    print(ans)

    return


if __name__ == "__main__":
    main()
