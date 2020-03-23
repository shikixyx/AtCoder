from operator import add
import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 解説見た
# 半分全列挙
# bit全探索

H, W, K = map(int, input().split())
MEIJI = []
for _ in range(H):
    MEIJI.append(list(map(int, list(input()))))

# 全部のカットを試す
INF = 10 ** 5
ans = INF
for h in range(2 ** (H - 1)):
    # 先に横の分割の数
    row = 1
    for i in range(H - 1):
        row += (h >> i) & 1

    num_cut = row - 1
    cnt = [0] * row

    #print("cut == ", h, "row == ", row)

    # 列は貪欲にカット
    for c in range(W):
        idx = 0
        tmp_cnt = [0] * row
        for r in range(H):

            if r != 0 and (h >> r - 1) & 1:
                idx += 1

            tmp_cnt[idx] += MEIJI[r][c]

        # チェック
        new_cnt = list(map(add, cnt, tmp_cnt))

        if any([K < x for x in new_cnt]):
            # 1列だけでもK以下が作れないならばbreak
            if any([K < x for x in tmp_cnt]):
                num_cut = INF
                break

            cnt = tmp_cnt
            num_cut += 1
        else:
            cnt = new_cnt

        #print("column:", c, tmp_cnt)

    ans = min(num_cut, ans)

print(ans)
