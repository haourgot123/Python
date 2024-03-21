from math import *

def fibo(n):
    f1 = 1
    f2 = 1
    if n == 1:
        print(f1)
    else :
        print(f1,f2,sep = "\n")
    for i in range(2, n ):
        fn = f1 + f2
        print(fn, sep = "\n")
        f1 = f2
        f2 = fn


if __name__ == "__main__":
    n = int(input())
    fibo(n)