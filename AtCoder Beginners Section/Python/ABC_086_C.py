N = int(input())

# POINTは配列に
POINT = []
for _ in range(N):
    t, x, y = map(int, input().split())
    POINT.append([t, x, y])

# こんな書き方も
# POINT = [[int(x) for x in input().split()] for _ in range(N)]

# t秒で移動できるか？
# できるとして、偶数ステップか？
prev_xy = (0, 0)
prev_t = 0
ans = 'Yes'
for t, x, y in POINT:
    d = abs(prev_xy[0] - x) + abs(prev_xy[1] - y)
    t2 = t - prev_t
    if d > t2 or (d - t2) % 2 != 0:
        ans = 'No'
        break
    prev_xy = (x, y)
    prev_t = t


print(ans)
