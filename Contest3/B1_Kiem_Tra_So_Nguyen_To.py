from math import *

def ngto(n):
    for i in range(2,int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True





if __name__ == "__main__":
    n = int(input())
    if ngto(n) == True:
        print("YES")
    else:
        print("NO")