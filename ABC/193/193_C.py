import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


# n以下の素数列挙(O(n log(n))
def primes(n):
    ans = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            ans.append(i)
    return ans


def main():
    N = int(input())
    if N <= 3:
        print(0)
        return

    ps = primes(N)
    t = 0
    for p in ps:
        for i in range(2, 20):
            if pow(p, i) <= N:
                t += 1
                print(p, i)
            else:
                break

    print(N - t)

    return


if __name__ == "__main__":
    main()
