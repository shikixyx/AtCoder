S = input()

# 合致するものがあればansをYESに書き換える
# 後ろから見ていく
i = len(S)
ans = 'NO'
while True:
    if i == 0:
        ans = 'YES'
        break

    # 5文字
    s1 = S[i - 5:i]
    if s1 == 'dream' or s1 == 'erase':
        i = i - 5
        continue

    # 6文字
    s2 = S[i - 6:i]
    if s2 == 'eraser':
        i = i - 6
        continue

    # 7文字
    s3 = S[i - 7:i]
    if s3 == 'dreamer':
        i = i - 7
        continue

    break

print(ans)
