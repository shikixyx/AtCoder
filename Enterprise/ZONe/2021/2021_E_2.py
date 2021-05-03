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
    COST_2 = [[10 ** 9] * C for _ in range(R)]
    COST[0][0] = 0
    Q = []
    heapq.heappush(Q, (A[0][0], 0, 1, 0))
    heapq.heappush(Q, (B[0][0], 1, 0, 0))

    while Q:
        cost, r, c, type = heapq.heappop(Q)
        # if cost > COST[r][c]:
        # continue

        if type == 1:
            ## 表
            nc = cost + 1
            if nc < COST[r][c]:
                heapq.heappush(Q, (nc, r, c, 0))
                COST[r][c] = nc

            ## 上
            if r > 0 and nc < COST_2[r - 1][c]:
                heapq.heappush(Q, (nc, r - 1, c, 1))
                COST_2[r - 1][c] = nc

            continue

        if r == R - 1 and c == C - 1:
            break

        COST[r][c] = cost

        ## 右
        if c < (C - 1):
            nc = cost + A[r][c]
            if nc < COST[r][c + 1]:
                heapq.heappush(Q, (nc, r, c + 1, 0))
                COST[r][c + 1] = nc

        ## 左
        if c > 0:
            nc = cost + A[r][c - 1]
            if nc < COST[r][c - 1]:
                heapq.heappush(Q, (nc, r, c - 1, 0))
                COST[r][c - 1] = nc

        ## 下
        if r < (R - 1):
            nc = cost + B[r][c]
            if nc < COST[r + 1][c]:
                heapq.heappush(Q, (nc, r + 1, c, 0))
                COST[r + 1][c] = nc

        ## 上
        if r > 0:
            nc = cost + 1
            if nc < COST_2[r - 1][c]:
                heapq.heappush(Q, (nc, r - 1, c, 1))
                COST_2[r - 1][c] = nc

        # print(COST)
        # print(COST_2)
    print(COST[R - 1][C - 1])

    return


if __name__ == "__main__":
    main()
