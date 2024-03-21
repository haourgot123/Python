from math import *

def tong(n):
    sum  = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x : (tong(x),x))    
    for i in range(len(a)):
        print(a[i], end = " ")