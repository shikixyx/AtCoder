## 問題

# 入力
# n (1 <= n <= 10 ** 5)
# s1, s2, ..., sn (siは長さ1以上10以下の文字列)

# 出力
# "しりとり" から始めて、最後に "ん" で終わる単語の数の最小値


import sys
import heapq

INF = 10 ** 9
sys.setrecursionlimit(10 ** 7)

def main():
    # input
    n = int(input())
    ss = [input() for _ in range(n)]

    # create graph
    path = [[INF] * 200 for _ in range (200)]

    for i in range(n):
        s = ss[i]
        start = convert(s[0])
        end = convert(s[-1])

        if (start == end):
            continue

        path[start][end] = 1

    # dijkstra
    dist = [INF] * 200
    dist[convert("り")] = 0
    q = [(0, convert("り"))]

    while q:
        d, v = heapq.heappop(q)

        if dist[v] < d:
            continue

        for i in range(100):
            if path[v][i] == INF:
                continue

            if dist[i] > dist[v] + path[v][i]:
                dist[i] = dist[v] + path[v][i]
                heapq.heappush(q, (dist[i], i))

    if dist[convert("ん")] == INF:
        print(-1)
    else:
        print(dist[convert("ん")])

def convert(s):
    return ord(s) - ord('ぁ')



if __name__ == '__main__':
    main()