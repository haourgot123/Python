from math import *

def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
        


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for i in range(len(a)):
        if snt(a[i]):
          sum += a[i]
          cnt += 1
    sum /= cnt
    print("%.3f" %sum)  