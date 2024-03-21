from math import *



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = min(a)
    ans = 0
    for i in range(len(a)):
        if x == a[i]:
            ans += 1
    print(ans)