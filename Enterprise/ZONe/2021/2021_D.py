import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = list(input())
    from_right = True
    ans = deque([])

    for i in range(len(S)):
        s = S[i]
        if s == "R":
            from_right = not (from_right)
        else:
            if from_right:
                ans.append(s)
            else:
                ans.appendleft(s)

    ans = list(ans)

    if not from_right:
        ans = ans[::-1]

    stack = []
    for s in ans:
        if stack and s == stack[-1]:
            stack.pop()
            continue
        else:
            stack.append(s)

    print("".join(stack))

    return


if __name__ == "__main__":
    main()
