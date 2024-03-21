from math import *

def scp(n):
    res = isqrt(n)
    if res**2 == n: return True
    else : return False

if __name__ == "__main__":
    n = int(input())
    if scp(n) == True: print("YES")
    else : print("NO")