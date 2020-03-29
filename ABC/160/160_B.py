import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

X = int(input())

ans = 0

fv = X // 500
ans += fv * 1000

X -= fv * 500

five = X // 5
ans += five * 5

print(ans)
