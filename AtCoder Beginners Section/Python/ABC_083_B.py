# 入力
N, A, B = map(int, input().split())

cnt = 0

# 1-Nまで
for n in range(1, N + 1):
    # 各桁の和
    digit_sum = 0
    for s in str(n):
        digit_sum += int(s)

    if A <= digit_sum <= B:
        cnt += n

print(cnt)
