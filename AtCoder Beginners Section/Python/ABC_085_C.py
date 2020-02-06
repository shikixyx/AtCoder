N, Y = map(int, input().split())

# 1万円札a枚
# 5千円札b枚
# 千円札c枚

x, y, z = -1, -1, -1
for a in range(N + 1):
    for b in range(N + 1):
        if a + b > N:
            continue

        c = N - a - b
        s = 10000 * a + 5000 * b + 1000 * c

        if s == Y:
            x, y, z = a, b, c
            break


print(x, y, z)
