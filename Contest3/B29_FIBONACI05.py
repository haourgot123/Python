from math import *

def check(n):
    if n == 1:
        return True
    f0 = 0
    f1 = 1
    for i in range(2,130):
        fn = f1 + f0
        if fn  == n:
            return True
        elif fn > n:
            return False
        f0 = f1 
        f1 = fn



if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        if check(n):
            print("YES")
        else:
            print("NO")
        t -= 1