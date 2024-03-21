from math import *


def check(a,i,n):
    if i >= n:
        return True
    else:
        if a[i] <= a[i - 1]:
            return False
        else:
            return check(a, i + 1, n)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    if check(a, 1, n):
        print("YES")
    else:
        print("NO")
    