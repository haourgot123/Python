from math import *

def binary_search(a, l, r, x):
    if l > r:
        return False
    else:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            return binary_search(a,l, mid  - 1, x)
        else:
            return binary_search(a, mid + 1, r, x)
        

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    t = int(input())
    while t > 0:
        x = int(input())
        if binary_search(a,0, n - 1, x):
            print("YES")
        else:
            print("NO")
        t -= 1
            