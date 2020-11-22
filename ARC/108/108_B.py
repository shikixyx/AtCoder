import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    S = list(input())

    stack = []

    for s in S:
        stack.append(s)
        if len(stack) >= 3:
            l3 = stack[-3:]
            if l3[0] == "f" and l3[1] == "o" and l3[2] == "x":
                for _ in range(3):
                    stack.pop()

    ans = len(stack)
    print(ans)

    return


if __name__ == "__main__":
    main()
