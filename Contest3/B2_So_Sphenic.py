from math import *


def check_sphenic(n):
    for i in range (2,n):
        cnt = 0
        while n % i == 0:
            cnt += 1
            if cnt == 2:
                return False
            n = n / i
    return True




if __name__ == "__main__":
    n = int(input())
    if check_sphenic(n) == True:
        print("1")
    else:
        print("0")