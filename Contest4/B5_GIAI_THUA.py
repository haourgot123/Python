from math import *

def gt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * gt(n-1)



if __name__ == "__main__":
    n = int(input())
    ans = gt(n)
    print(ans)