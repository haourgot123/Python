from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    f = []
    f.append(a[0])
    for i in range(1,n):
        f.append(f[i - 1] + a[i])
    for i in range(len(f)):
        print(f[i], end = " ")