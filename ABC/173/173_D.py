import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

if N == 2:
    print(A[0])
    exit()
elif N == 3:
    print(A[0] + A[1])
    exit()

ans = A[0]
N -= 2

for i in range(1, N):
    if N == 0:
        break
    a = A[i]
    c = min(2, N)
    ans += a * c
    N -= c

print(ans)


"""
if N == 2:
    print(A[0])
    exit()
elif N == 3:
    print(A[0] + A[1])
    exit()

ans = sum(A[:-2]) + A[1]
print(ans)
"""
