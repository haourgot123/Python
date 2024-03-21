from math import *

def Dec2Hex(n):
    if n != 0:
        Dec2Hex(n // 16)
        r = n % 16
        if r < 10:
            print(r, end = "")
        else:
            print(chr(r + 55), end  = "")





if __name__ == "__main__":
    n = int(input())
    if n == 0 :
        print("0")
    else : Dec2Hex(n)