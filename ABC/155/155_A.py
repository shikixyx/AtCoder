import sys
sys.setrecursionlimit(10 ** 7)

A, B, C = map(int, input().split())

ans = 'No'
if A == B and B == C:
    ans = 'No'
elif A == B or B == C or A == C:
    ans = 'Yes'

print(ans)
