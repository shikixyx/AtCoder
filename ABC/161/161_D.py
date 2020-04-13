import bisect
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# ゴリ押し

K = int(input())

cnt = 0
LUN = [[0] * 10 for _ in range(11)]
LUN_AC = [[0] * 10 for _ in range(11)]
LUN[0] = [1] * 10

cnt = 0
for i in range(1, 11):
    # i桁目のLUN数
    for d in range(10):
        c = 0
        c += LUN[i-1][d - 1] if 1 <= d and i > 1 else 0
        c += LUN[i - 1][d]
        c += LUN[i - 1][d + 1] if d < 9 and i > 1 else 0

        if d != 0:
            cnt += c

        LUN[i][d] = c

        #print("i,d,cnt", i, d, cnt)

        if K <= cnt:
            break

    if K <= cnt:
        break

#print(i, d)

keta = i
rest = K - cnt + c

ans = []
ans.append(d)

for i in range(keta - 1, 0, -1):
    #print("i,d,rest", i, d, rest)
    c1 = LUN[i][d - 1] if 1 <= d else 0
    if rest <= c1:
        ans.append(d - 1)
        d = d - 1
        continue
    else:
        rest -= c1

    c2 = LUN[i][d]

    if rest <= c2:
        ans.append(d)
        continue
    else:
        rest -= c2

    c3 = LUN[i][d + 1] if d < 9 else 0

    if rest <= c3:
        ans.append(d + 1)
        d = d + 1
        continue
    else:
        rest -= c3

    if rest >= 0:
        print(-1)
        exit()

print("".join(map(str, ans)))
