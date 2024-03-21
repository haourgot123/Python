from math import *





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = [1] * n
    c = [0] * n
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] == a[j] and c[j] == 0:
                b[i] += 1
                c[j] = 1
    for i in range(len(a)):
        if c[i] == 0:
            print(a[i], b[i])