from math import *

def ham1(a, l, r, x):
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            res = mid
            r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return res

def ham2(a, l, r, x):
    res =  -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            res = mid
            l = mid + 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return res
            



if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    for i in range(len(a)):
        p1, p2 = ham1(a, i + 1, n - 1, a[i] + x), ham2(a, i + 1, n - 1, x + a[i])
        if p1 != - 1:
            ans += p2 - p1 + 1
    if ans == 0:
        print("-1")
    else:
        print("1")