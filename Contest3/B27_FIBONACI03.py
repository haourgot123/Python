from math import *


def fibonaci(n):
    if n == 1: return 1
    f0 = 1
    f1 = 1
    for i in range(2,150):
        fn = f0 + f1
        if fn >= n:
            return fn
        f0 =f1
        f1 = fn
        
        


if __name__ == "__main__":
    n = int(input())
    ans = fibonaci(n)
    print(ans)