from math import *

MOD  = 1e9 + 7
def binpow(a,b):
    if b == 0:
        return a
    X = binpow(a, b // 2)
    if b % 2 == 1:
        return X * X * a % MOD
    else:
        return X * X % MOD

if __name__ == "__main__":
    a,b = map(int, input().split())
    ans = binpow(a,b)
    print(ans)