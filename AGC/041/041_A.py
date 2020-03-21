N, A, B = map(int, input().split())

ans = 0

sml = A
big = B

if (A-B) > 0:
    sml = B
    big = A

if (A - B) % 2 == 0:
    ans = (big - sml) // 2
else:
    s = sml - 1
    b = N - big

    if s > b:
        t = (big - sml) + (2*b) + 1
    else:
        t = (big - sml) + (2*s) + 1

    ans = t // 2

print(ans)
