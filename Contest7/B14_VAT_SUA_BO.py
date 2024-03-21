from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = a[0]
    for i in range(1, n):
        if a[i] - i >= 0:
            ans += a[i] - i
    
    print(ans)