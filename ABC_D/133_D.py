import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 17min

N = int(input())
A = list(map(int, input().split()))

al = sum(A)

x = al - sum(A[1::2]) * 2

ans = []
ans.append(x)

for i in range(N-1):
    x = A[i] * 2 - x
    ans.append(x)

print(' '.join(map(str, ans)))
