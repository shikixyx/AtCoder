import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = map(int, input().split())

if c - a - b <= 0:
    ans = 'No'
elif 4 * a * b < pow((c - a - b), 2):
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
