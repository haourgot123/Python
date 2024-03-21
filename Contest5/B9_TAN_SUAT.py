from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b  = [0] * n
    c = [1] * n
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                c[i] += 1
                b[j] = 1
    for i in range(len(b)):
        if b[i] == 0:
            print(a[i], c[i])