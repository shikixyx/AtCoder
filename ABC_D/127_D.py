import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 25min
# 2020/03/10

N, M = map(int, readline().split())
A = list(map(int, readline().split()))
A.sort()

BC = [[int(x) for x in readline().split()] for _ in range(M)]
BC.sort(key=lambda x: (-x[1], -x[0]))

BC_idx = 0

for i in range(N):
    a = A[i]

    b, c = BC[BC_idx]
    if a < c:
        A[i] = c
        b -= 1

        if b == 0:
            BC_idx += 1
            if BC_idx == M:
                break
        else:
            BC[BC_idx][0] = b
    else:
        break

print(sum(A))
