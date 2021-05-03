import sys
import bisect

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    IDX = []
    POINTS = []
    for i in range(5):
        T = []
        for j in range(N):
            T.append((P[j][i], j))

        T.sort()

        idxs = []
        points = []
        for j in range(N):
            p, n = T[j]
            idxs.append(n)
            points.append(p)

        IDX.append(idxs)
        POINTS.append(points)

    left = 1
    right = 10 ** 9

    while (right - left) != 1:
        mid = (left + right) // 2

        people = set()
        for i in range(5):
            t = bisect.bisect_left(POINTS[i], mid)

            if i == 0:
                people = set(IDX[i][t:])
            else:
                people &= set(IDX[i][t:])

            print(people)

        if len(people) >= 3:
            left = mid
        else:
            right = mid

    print(left)

    return


if __name__ == "__main__":
    main()
