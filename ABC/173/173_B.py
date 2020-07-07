import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
S = [input() for _ in range(N)]

C = Counter(S)

print("AC x {}".format(C["AC"]))
print("WA x {}".format(C["WA"]))
print("TLE x {}".format(C["TLE"]))
print("RE x {}".format(C["RE"]))
