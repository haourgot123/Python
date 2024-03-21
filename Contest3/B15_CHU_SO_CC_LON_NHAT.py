from math import *

def snt(n):
    if n < 2 : return False
    if n == 2: return True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def digit_end(n):
    ans = -1
    tmp = n
    while n > 0:
        ans = max (ans, n % 10)
        n //= 10
    return tmp % 10 == ans


if __name__ == "__main__":
    n = int(input())
    dem  = 0
    for i in range(2, n+1):
        if snt(i) and digit_end(i):
            dem += 1
            print(i, end = " ")
    print()
    print(dem)