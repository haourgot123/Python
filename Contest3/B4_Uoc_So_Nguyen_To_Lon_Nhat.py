from math import *

def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
        

def uocso(n):
    res = -1
    for i in range (1,isqrt(n) + 1):
        if n % i == 0:
            if check(i) == True:
                res = max(res, i)
            if i != n / i:
                if check(int(n/i)) == True:
                    res = max(res, n/i)
    return res            



if __name__  == "__main__":
    t = int(input())
    while t >= 1:
        n = int(input())
        print(int(uocso(n)))
        t = t - 1