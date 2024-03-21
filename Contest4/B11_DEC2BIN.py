from math import *


def Dec2Bin(n):
    if n < 2:
        print(n%2, end = "")
        return n
    Dec2Bin(n // 2)
    print(n % 2, end= "")


if __name__ == "__main__":
    n = int(input())
    Dec2Bin(n)