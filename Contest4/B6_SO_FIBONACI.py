from math import *

def fibonaci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)


if __name__ == "__main__":
    n = int(input())
    ans = fibonaci(n)
    print(ans)