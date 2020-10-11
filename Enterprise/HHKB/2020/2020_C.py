import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
P = list(map(int, input().split()))

NUM_LIST = [False] * 200100
ANS = []

idx = 0
for p in P:
    NUM_LIST[p] = True

    while NUM_LIST[idx]:
        idx += 1

    ANS.append(idx)

print("\n".join(map(str, ANS)))

