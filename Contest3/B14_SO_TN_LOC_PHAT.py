from math import *

def tn(n):
    tmp = n
    sum = 0
    while n > 0:
        sum = sum*10 + n % 10
        n //= 10
    return tmp == sum

def digit_6(n):
    while n > 0:
        x = n % 10
        if x == 6:
            return True
        n //= 10
    return False

def sum_8(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum % 10 == 8
if __name__ == "__main__":
    a,b = map(int, input().split())
    for i in range(a,b+1):
        if tn(i) and digit_6(i) and sum_8(i):
            print(i, end = " ")