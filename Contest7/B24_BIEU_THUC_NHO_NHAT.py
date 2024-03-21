from math import *



if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[0]
    a[1:]  = sorted(a[1:], reverse = True)
    for i in range(1, n):
        if i <= k:
            ans += a[i]
        else:
            ans -= a[i]
    print(ans)