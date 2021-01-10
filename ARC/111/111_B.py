import sys
import networkx as nx

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    group1 = list(map(str, range(1, N + 1)))
    group2 = []

    g = nx.Graph()
    g.add_nodes_from(group1, bipartite=0)

    E = []
    for i in range(N):
        a, b = AB[i]
        E += [(str(i + 1), a), (str(i + 1), b)]
        group2 += [a, b]

    group2 = list(set(group2))
    g.add_nodes_from(group2, bipartite=1)

    g.add_edges_from(E)
    # L = bipartite.matching.hopcroft_karp_matching(g, group1)
    L = nx.bipartite.matching.eppstein_matching(g, group1)

    print(len(L) // 2)

    return


if __name__ == "__main__":
    main()
