import sys
import heapq
import itertools

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    H = []
    for i in range(5):
        hp = []
        for j in range(N):
            heapq.heappush(hp, (-P[j][i], j))

        H.append(hp)

    ans = 0

    for a, b in itertools.permutations(range(N), 2):
        p = []
        for i in range(5):
            t = max(P[a][i], P[b][i])
            p.append((t, i))

        p.sort()

        if p[0][0] == p[1][0]:
            ans = max(ans, p[0][0])
            continue

        sml = p[0][0]
        big = p[1][0]
        sml_idx = p[0][1]

        # print(a, b, p, sml_idx)

        ## でかいのがあるか？
        poped = []
        while True:
            t = heapq.heappop(H[sml_idx])
            poped.append(t)

            if t[1] == a or t[1] == b:
                continue

            if -t[0] < big:
                ans = max(ans, sml)
            else:
                ans = max(ans, big)

            break

        for t in poped:
            heapq.heappush(H[sml_idx], t)

    print(ans)

    return


if __name__ == "__main__":
    main()
