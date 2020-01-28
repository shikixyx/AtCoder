import sys
sys.setrecursionlimit(10 ** 7)

# 素数判定

N = int(input())

is_prime = True

for i in range(2, N):
    if i * i > N:
        break

    if N % i == 0:
        is_prime = False
        break

if is_prime:
    print('YES')
else:
    print('NO')
