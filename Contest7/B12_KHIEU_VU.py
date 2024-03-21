from math import *





if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] > b[j]:
            ans += 1
            j += 1
            i += 1
        else:
            i += 1
    print(ans)
        