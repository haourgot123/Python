from math import *

def check(n):
    for i in range(0,n // 111 + 1):
        if  (n - i * 111) % 11 == 0:
            return True
    return False



if __name__ == "__main__":
    n = int(input())
    res = "YES" if check(n) else "NO"
    print(res)