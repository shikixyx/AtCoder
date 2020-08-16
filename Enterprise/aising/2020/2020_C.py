import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

CNT = [0] * 10010
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            f = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if f > N:
                continue

            CNT[f] += 1

for i in range(1, N + 1):
    print(CNT[i])
