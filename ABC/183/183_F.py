import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # xの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # xとyを統合する
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    # xとyが同じグループかどうか判定する
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xのメンバーの要素を返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(Q)]

    U = UnionFind(N)
    GRP = [defaultdict(int) for _ in range(N)]

    for i in range(N):
        c = C[i]
        GRP[i][c] += 1

    ans = []
    for op, x, y in Q:
        if op == 1:
            if U.same(x - 1, y - 1):
                continue

            rx = U.find(x - 1)
            ry = U.find(y - 1)
            gx = GRP[rx]
            gy = GRP[ry]
            new_g = unite(gx, gy)

            U.union(x - 1, y - 1)
            r = U.find(x - 1)
            GRP[r] = new_g

        if op == 2:
            r = U.find(x - 1)
            ans.append(GRP[r][y])

    print("\n".join(map(str, ans)))

    return


def unite(x, y):
    if len(x) < len(y):
        x, y = y, x
    for k, v in y.items():
        x[k] += v

    return x


if __name__ == "__main__":
    main()
