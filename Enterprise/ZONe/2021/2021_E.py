import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    R, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(R)]
    B = [list(map(int, input().split())) for _ in range(R - 1)]

    COST = [[10 ** 9] * C for _ in range(R)]
    COST[0][0] = 0
    Q = []
    heapq.heappush(Q, (A[0][0], 0, 1))
    heapq.heappush(Q, (B[0][0], 1, 0))

    while Q:
        cost, r, c = heapq.heappop(Q)
        if cost > COST[r][c]:
            continue

        # print(r, c)

        COST[r][c] = cost

        if r == R - 1 and c == C - 1:
            break

        ## 右
        if c < (C - 1):
            nc = cost + A[r][c]
            if nc < COST[r][c + 1]:
                heapq.heappush(Q, (nc, r, c + 1))
                COST[r][c + 1] = nc

        ## 左
        if c > 0:
            nc = cost + A[r][c - 1]
            if nc < COST[r][c - 1]:
                heapq.heappush(Q, (nc, r, c - 1))
                COST[r][c - 1] = nc

        ## 下
        if r < (R - 1):
            nc = cost + B[r][c]
            if nc < COST[r + 1][c]:
                heapq.heappush(Q, (nc, r + 1, c))
                COST[r + 1][c] = nc

        ## 上
        if r > 0:
            for i in range(1, r + 1):
                nc = cost + (1 + i)
                if nc < COST[r - i][c]:
                    heapq.heappush(Q, (nc, r - i, c))
                    COST[r - 1][c] = nc

        # print(COST)
    print(COST[R - 1][C - 1])

    return


if __name__ == "__main__":
    main()
