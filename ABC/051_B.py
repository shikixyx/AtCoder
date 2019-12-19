k,s = map(int,input().split())
cnt = 0
z = list(range(k+1))

for x in range(k+1):
    for y in range(k+1):
        m = s - x - y
        if 0 <= m & m <= k:
            cnt += 1

print(cnt)