from math import *

def ucln(a,b):
    if b == 0:
        return a
    return ucln(b, a%b)

def bcnn(a,b):
    return int((a * b)/ucln(a,b))


if __name__ == "__main__":
    a,b = map(int, input().split())
    print(ucln(a,b), bcnn(a,b))
    