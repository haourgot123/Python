from math import *

def locphat(n):
    while n > 0:
        if n % 10 != 0 and n % 10 != 6 and n % 10 != 8:
            return False
        n //= 10
    return True



if __name__ == "__main__":
    n = int(input())
    if locphat(n):
        print("1")
    else:
        print("0")