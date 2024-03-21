from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [1] * n
    c = [0] * n
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] == a[j] and c[j] == 0:
                b[i] += 1
                c[j] = 1
    x = max(b)
    for i in range(len(a)):
        if x == b[i]:
            print(a[i], b[i])
            break