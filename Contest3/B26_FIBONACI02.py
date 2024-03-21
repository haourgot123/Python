from math import *


def fibobnaci(n):
    if n == 0 or n == 1:
        return True
    f0 = 0 
    f1 = 1
    for i in range(2,150):
        fn = f0 + f1
        if fn == n:
            return True
        elif fn > n:
            return False
        f1 = f2
        f2 = fn
        
        
        




if __name__ == "__main__":
    n =int(input())
    if fibobnaci(n):
        print("YES")
    else:
        print("NO")