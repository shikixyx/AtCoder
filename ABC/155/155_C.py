import sys
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(10 ** 7)

N = int(input())
SS = [input() for _ in range(N)]

cnt = defaultdict(int)

for s in SS:
    cnt[s] += 1

cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)

ans = deque([])
mx = -1
for i, x in cnt:
    if mx == -1:
        mx = x
    elif mx != x:
        break
    ans.appendleft(i)

print("\n".join(ans))
