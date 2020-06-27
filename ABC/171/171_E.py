import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))

CNT = [0] * 30
bit_list = []
for a in A:
    bit = [0] * 30

    for i in range(30):
        bit[i] = a & 1
        CNT[i] += bit[i]
        a >>= 1

    bit_list.append(bit)

print(CNT)

T = [x // (N - 1) for x in CNT]

print(T)

ANS = []
for bit in bit_list:
    a = 0
    c = 1
    for i in range(30):
        a += (T[i] - bit[i]) * c
        c *= 2

    ANS.append(a)

print(" ".join(map(str, ANS)))

