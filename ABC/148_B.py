from collections import deque

n = int(input())
S, T = map(deque, input().split())
st = ''

for i in range(n):
    s = S.popleft()
    t = T.popleft()
    st += s
    st += t

print(st)
