from math import *



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 10 ** 9 + 1
    for i in range(1, len(a)):
        if a[i] !=  a[i - 1]:
            ans = min(ans, a[i] - a[i - 1])
        else:
            ans = 0
            break
    print(ans)
        