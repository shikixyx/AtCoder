import sys
import networkx as nx
from networkx.algorithms import bipartite

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N, M, Q = map(int, input().split())
    WV = [0] + [list(map(int, input().split())) for _ in range(N)]
    X = [0] + list(map(int, input().split()))
    QUERY = [list(map(int, input().split())) for _ in range(Q)]

    from_nodes = list(range(1, N+1))

    ans = []
    for i in range(Q):
        L, R = QUERY[i]
        to_nodes = [x for x in range(1, M+1) if not L <= x <= R]
        g = nx.Graph()
        g.add_nodes_from(from_nodes, bipartite=0)
        g.add_nodes_from(to_nodes, bipartite=1)

        for j in from_nodes:
            W, V = WV[j]
            for k in to_nodes:
                if W <= X[k]:
                    g.add_edge(j, k, weight=V)

        nx.draw(g)

        E = nx.algorithms.matching.max_weight_matching(g)
        print(E)

    return


if __name__ == "__main__":
    main()
