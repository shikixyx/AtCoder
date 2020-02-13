import sys
import math
sys.setrecursionlimit(10 ** 7)

# 桁DP
# 再帰

N = input()
K = int(input())
lenN = len(N)


# 組み合わせの数
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


# i桁目から
# 残りk個 Non-Zero
# Nよりもsmallerか？
# というときの組み合わせの数
def CntAlmostZero(i, k, smaller):
    # N桁まで取り出した時
    if i == lenN:
        if k == 0:
            return 1
        else:
            return 0

    if k == 0:
        return 1

    # Nよりも小さい時
    if smaller:
        # 残りの桁でK個使える時
        if (lenN - i) >= k:
            return comb(lenN - i, k) * (9 ** k)
        # 無理なら 0
        else:
            return 0
    # 前がNと同じ桁の時(初期は0なので必ずこっち)
    else:
        # 見てる桁が0の時
        if N[i] == '0':
            return CntAlmostZero(i + 1, k, False)
        # 見てる桁が0以外の時
        else:
            # 0だったら
            zero = CntAlmostZero(i+1, k, True)
            # 同じだったら
            same = CntAlmostZero(i+1, k-1, False)
            # その間だったら
            aida = CntAlmostZero(i+1, k-1, True) * (int(N[i]) - 1)

            return zero + same + aida

    return 1


ans = CntAlmostZero(0, K, False)
print(ans)
