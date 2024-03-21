from math import *



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    dem = 0
    for i in range(len(a)):
        if i % 2 == 0 and a[i] % 2 == 0:
            dem = 1
            print(a[i], end = " ")
    if dem == 0:
        print("NONE")