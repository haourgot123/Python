from math import *

def tong(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n //= 10
    return sum

def smith(n):
    tong1 = tong(n)
    tong2 = 0
    tmp = n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                tong2  = tong2  + tong(i)
                n //= i
    if tmp == n:
        return False
    if n > 1:
        tong2 = tong2 + tong(n)
    return tong1 == tong2
        
        



if __name__ == "__main__":
    n = int(input())
    if(smith(n)):
        print("YES")
    else:
        print("NO")