from math import *

def lcm(a,b):
    return a * b //gcd(a,b)


if __name__ == "__main__":
    x,y,z,n = map(int, input().split())
    bcnn = lcm(lcm(x,y),z)
    tmp = 10 ** (n - 1)
    ans = (bcnn + tmp - 1) // bcnn * bcnn
    if ans < 10 ** n:
        print(ans)
    else:
        print("-1") 
    