import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if Z == 0:
        break

    a = A[i]
    man = a // 10000
    if man == 0:
        continue
    num = man if man <= Z else Z
    A[i] -= num * 10000
    Z -= num

A.sort(key=lambda x: (x//10000, x % 10000), reverse=True)

for i in range(N):
    a = A[i]
    if Z == 0:
        break
    if a < 0:
        continue
    elif a == 0:
        a += 1

    man = -(-a // 10000)

    num = man if man <= Z else Z
    A[i] -= num * 10000
    Z -= num


for i in range(N):
    if Y == 0:
        break

    a = A[i]

    if a < 0:
        continue

    gosen = a // 5000
    if gosen == 0:
        continue
    num = gosen if gosen <= Y else Y
    A[i] -= num * 5000
    Y -= num


A.sort(key=lambda x: (x//5000, x % 5000), reverse=True)

for i in range(N):
    a = A[i]
    if Y == 0:
        break
    if a < 0:
        continue
    elif a == 0:
        a += 1

    gosen = -(-a // 5000)

    num = gosen if gosen <= Y else Y
    A[i] -= num * 5000
    Y -= num


for i in range(N):
    a = A[i]

    if a < 0:
        continue

    if a == 0:
        a += 1

    if X == 0:
        print('No')
        exit()

    sen = -(-a // 1000)
    num = sen if sen <= X else X
    a -= num * 1000
    X -= num

    if a >= 0:
        print('No')
        exit()


print('Yes')
exit()
