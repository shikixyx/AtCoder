# 入力を受け取る
A = int(input())
B = int(input())
C = int(input())
X = int(input())


# 何通りあるか？
cnt = 0

# 全通り試す
# 500円玉がa枚
# 100円玉がb枚
# 50円玉がc枚
# 変数名に注意
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            s = 500 * a + 100 * b + 50 * c
            if X == s:
                cnt += 1

print(cnt)
