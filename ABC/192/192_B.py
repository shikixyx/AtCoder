import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = input()
    flg = True
    for i in range(len(S)):
        s = S[i]

        # 奇数
        if i % 2 == 0:
            if s.islower():
                pass
            else:
                flg = False

        elif i % 2 == 1:
            if s.islower():
                flg = False

    if flg:
        print("Yes")
    else:
        print("No")

    return


if __name__ == "__main__":
    main()
