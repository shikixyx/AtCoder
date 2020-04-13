import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

# 時間外
# AC


# nの約数列挙
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない


div_n = divisor(N)
div_n1 = divisor(N - 1)

ans = []
for d in div_n:
    if d == 1:
        continue
    n = N
    while n % d == 0:
        n //= d

    if n % d == 1 or n == 1:
        ans.append(d)

for d in div_n1:
    if d == 1:
        continue
    if N % d == 0:
        nd = N // d
        if nd % d == 1 or nd % d == 0:
            ans.append(d)
    else:
        ans.append(d)


ans = list(set(ans))
# print(ans)
print(len(ans))
