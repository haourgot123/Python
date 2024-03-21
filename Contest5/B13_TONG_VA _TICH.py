from math import *



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    tong = 0
    tich = 1
    for i in range(len(a)):
        tong = (tong + a[i]) % (10 ** 9 + 7)
        tich = (tich * a[i]) % (10 ** 9 + 7)
    print(tong, tich, sep = "\n")
        