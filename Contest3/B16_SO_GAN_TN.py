from math import *

def count_digit(n):
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res

def tn(n):
    tmp = n
    sum = 0
    while n > 0:
        sum = sum * 10 + n % 10
        n //= 10
    return tmp == sum    

def check(n):
    x = n % 10
    y = n // (10 ** (count_digit(n) - 1))
    n //= 10
    n %= (10 ** (count_digit(n) - 1))
    if x == y * 2:
        return tn(n)
    elif y == x * 2:
        return tn(n)
    else:
        return False 
    
    
     


if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")