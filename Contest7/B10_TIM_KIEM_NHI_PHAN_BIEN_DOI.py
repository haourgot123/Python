from math import *

def ham1(a, l, r, x):
    index = - 1
    while l <= r:
        mid = (l + r) // 2 
        if a[mid] == x:
               index = mid
               r = mid - 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return index

def ham2(a, l, r, x):
    index = - 1
    while l <= r:
        mid = (l + r) // 2 
        if a[mid] == x:
               index = mid
               l = mid + 1
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return index

def ham3(a, l, r, x):
    index = - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    return index

def ham4(a, l, r, x):
    index = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    return index    

def ham5(a, l, r, x):
    tmp1 = ham1(a,l, r, x)
    tmp2 = ham2(a, l, r, x)
    if tmp1 == -1:
        return 0
    elif tmp1 == tmp2:
        return 1
    else:
        return tmp2 - tmp1 + 1
    

if __name__ == "__main__":
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans1 = ham1(a,0, n - 1, x)
    ans2 = ham2(a,0, n - 1, x)
    ans3 = ham3(a,0, n - 1, x)
    ans4 = ham4(a,0, n - 1, x)
    ans5 = ham5(a, 0,  n - 1, x)
    print(ans1, ans2, ans3, ans4, ans5, sep="\n")
    