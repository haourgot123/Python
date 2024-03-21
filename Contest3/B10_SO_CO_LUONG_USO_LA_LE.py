from math import *

def check(n):
    return sqrt(n) - isqrt(n) == 0

if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")