from math import *

def sum(n):
    if n == 1:
        return 1
    return 1/n + sum(n-1)


if __name__ == "__main__":
    n = int(input())
    ans = sum(n)
    print('%.3f' %ans)
    