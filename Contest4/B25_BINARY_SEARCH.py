from math import *

def binary_search(a, left, right, x):
    if left > right:
        return False

    mid  = (left + right) // 2
    if a[mid] == x:
        return True
    elif a[mid] < x:
        return binary_search(a,mid + 1, right, x)
    else:
        return binary_search(a,left, mid - 1, x)        


if __name__ == "__main__":
    n  = int(input())
    a = list(map(int, input().split()))
    x  = int(input())
    a.sort()
    if binary_search(a, 0, n - 1, x):
        print("1")
    else:
        print("0")