from math import *



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0, n):
        if a[i] >= 0:
            if (i - 1 >= 0 and a[i - 1] < 0) or (i + 1 < n and a[i + 1] < 0):
                print(a[i], end = " ")
        else:
            if (i - 1 >= 0 and a[i - 1] > 0) or (i + 1 < n and a[i + 1] > 0):
                print(a[i], end = " ")
            
            