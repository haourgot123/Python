from math import *


def sum_uoc_so(n):
    ans = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ans += i
            if i != n//i: ans += n//i
    return ans


if __name__ == "__main__":
    n = int(input())
    res = sum_uoc_so(n)
    print(res)