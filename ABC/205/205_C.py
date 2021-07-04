import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B, C = map(int, input().split())

    if A == B:
        print("=")
        return

    if C % 2 == 0 and (abs(A) == abs(B)):
        print("=")
        return

    # if A == 0:
    #     print("<")
    #     return

    # if B == 0:
    #     print(">")
    #     return

    ## 同符号
    if A * B >= 0:
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            else:
                print("<")
        else:
            if A > B:
                print(">")
            else:
                print("<")
    else:
        ## 逆符号

        ## 偶数乗
        if C % 2 == 0:
            if abs(A) > abs(B):
                print(">")
            else:
                print("<")
        else:
            ## 奇数
            if A < 0:
                print("<")
            else:
                print(">")

    return


if __name__ == "__main__":
    main()
