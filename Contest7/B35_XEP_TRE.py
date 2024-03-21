from math import *




if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l, r = 0, n - 1
    ans  = 0
    while l <= r:
        if a[l] + a[r] <= x:
            ans += 1
            l += 1
            r -= 1
        else:
            ans += 1
            r -= 1
    print(ans)