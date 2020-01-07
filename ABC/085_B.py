import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N = int(input())

A = [0] * N

for i in range(N):
    a = int(readline())
    A[i] = a

print(len(set(A)))
