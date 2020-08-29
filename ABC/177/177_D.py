import sys

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


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

U = UnionFind(N + 1)

for a, b in AB:
    if not U.same(a, b):
        U.union(a, b)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, U.size(i))

print(ans)

