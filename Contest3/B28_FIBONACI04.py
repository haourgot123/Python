from math import *

def snt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check_fibo(n):
    if n == 1:
        return True
    f0 = 0
    f1 = 1
    for i in range(2, 30):
        fn = f0 + f1
        if fn == n:
            return True
        elif fn > n:
            return False
        f0 = f1
        f1 = fn

def check_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return check_fibo(sum)

if __name__ == "__main__":
    n = int(input())
    for i in range(2, n + 1):
        if check_sum(i) and snt(i):
            print(i, end = " ")