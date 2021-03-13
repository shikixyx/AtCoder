import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    NUM = [0] * (N + 10)

    for i in range(M):
        NUM[A[i]] += 1

    candidate = []
    for i in range(N + 10):
        if NUM[i] > 0:
            continue

        candidate.append(i)

    heapq.heapify(candidate)

    ans = N + 10
    for i in range(N-M+1):
        while True:
            t = heapq.heappop(candidate)
            if NUM[t] == 0:
                ans = min(t, ans)
                heapq.heappush(candidate, t)
                break

        # print("i = {}: t = {}".format(i, t))

        if i == (N - M):
            break

        # 移動させる
        NUM[A[i]] -= 1
        NUM[A[i+M]] += 1

        if A[i] != A[i+M] and NUM[A[i]] == 0:
            heapq.heappush(candidate, A[i])

    print(ans)

    return


if __name__ == "__main__":
    main()
