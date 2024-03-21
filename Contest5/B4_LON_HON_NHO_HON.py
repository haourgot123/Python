from math import *






if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    ans1 = 0
    ans2 = 0
    for i in range(len(a)):
        if a[i] > x:
            ans1 += 1
        if a[i] < x:
            ans2 += 1
    print(ans2)
    print(ans1)