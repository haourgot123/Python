from math import *


if __name__ == "__main__":
    a,b = map(int, input().split())
    x = ceil(sqrt(a))
    y = isqrt(b)
    for i in range(x,y + 1):
        print(i**2, end = " ")
    