import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()
N = len(S)

ans = 'Yes'

mid1 = (N - 1) // 2
mid2 = ((N + 3) // 2) - 1

one = S[:mid1]
two = S[mid2:]


if not(one == one[::-1] and two == two[::-1]):
    ans = 'No'

if not (S == S[::-1]):
    ans = 'No'

print(ans)
