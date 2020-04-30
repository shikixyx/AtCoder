import sys


class RotatingNumbers:
    def findSolution(self, N, P, grid):
        return ["0 0 {} R".format(N)]


N = int(input())
P = int(input())
grid = [0] * N
for i in range(N):
    grid[i] = [0] * N
for i in range(N * N):
    grid[(int)(i / N)][(int)(i % N)] = int(input())

prog = RotatingNumbers()
ret = prog.findSolution(N, P, grid)
print(len(ret))
for st in ret:
    print(st)
sys.stdout.flush()
