import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = list(input())
    ans = ""
    for s in S[::-1]:
        if s == "6":
            ans += "9"
        elif s == "9":
            ans += "6"
        else:
            ans += s

    print(ans)

    return


if __name__ == "__main__":
    main()
