from math import *




if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    t = int(input())
    while t > 0:
        x = int(input())
        if x in s:
            print("YES")
        else:
            print("NO")
        t -= 1