from math import *

def sum(n):
    if n == 0:
        return 0
    return n ** 2 + sum(n -1)

if __name__ == "__main__":
    n = int(input())
    ans = sum(n)
    print(ans)