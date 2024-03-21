from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    res = a[0]
    ans = 1
    a.append(10 ** 18)
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            if cnt > ans:
                ans = cnt
                res = a[i - 1]
            cnt = 1
    print(res, ans) 