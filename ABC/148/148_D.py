from collections import deque

N = int(input())
A = deque(map(int, input().split()))

blk = 1
cnt = 0

for i in range(N):
    a = A.popleft()

    if a == blk:
        blk += 1
    else:
        cnt += 1

if blk == 1:
    cnt = '-1'

print(cnt)
