from math import *





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1,n):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans + 1)