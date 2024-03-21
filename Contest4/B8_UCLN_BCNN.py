from math import *

def lcm(a,b):
    return a * b // gcd(a,b)




if __name__ == "__main__":
    a,b = map(int, input().split())
    uc = gcd(a,b)
    bc = lcm(a,b)
    print(uc,bc)