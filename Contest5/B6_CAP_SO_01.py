from math import *





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    ans = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] == x:
                ans += 1
    print(ans)
        