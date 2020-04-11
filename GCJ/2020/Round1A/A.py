import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = int(readline())


def solve():
    N = int(readline())
    SS = [str(readline().rstrip().decode('utf-8')) for _ in range(N)]

    post = [(-len(S[1:]), S[1:]) for S in SS]
    post.sort()

    longest = post[0][1]
    ok = True
    for i in range(1, N):
        l, s = post[i]
        if s != longest[l:]:
            ok = False
            break

    ans = None
    if not ok:
        ans = '*'
    else:
        ans = longest

    return ''.join(ans)


ans = []
for i in range(1, T+1):
    t = solve()
    txt = "Case #{}: {}".format(i, t)
    ans.append(txt)

print('\n'.join(ans))
exit(0)
