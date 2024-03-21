from math import *

def snt(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def digit_number(n):
    sum  = 0
    while n > 0:
        x = n % 10
        sum += x
        if snt(x) == False:
            return False
        n //= 10
    return snt(sum)



if __name__ == "__main__":
    a,b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        if digit_number(i) and snt(i):
            ans += 1
    print(ans)