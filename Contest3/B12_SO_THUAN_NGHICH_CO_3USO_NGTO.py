from math import *

def snt(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def tn(n):
    sum = 0
    tmp = n
    while n > 0:
        sum = sum * 10 + n % 10
        n //= 10
    return sum == tmp

def uso_nto(n):
    ans = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            if snt(i):
                ans += 1
            if i != n // i:
                if snt(n//i):
                    ans += 1
    return ans >= 3                


if __name__ == "__main__":
    a,b = map(int, input().split())
    dem = 0
    for i in range(a,b+1):
        if tn(i) and uso_nto(i):
            dem += 1
            print(i, end = " ")
    if dem == 0: 
        print("-1")