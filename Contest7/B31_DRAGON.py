from math import *



if __name__ == "__main__":
    n, s = map(int, input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    a.sort(key = lambda x : x[0])
    for x, y in a:
        if x >= s:
            print("NO")
            exit()
        s += y
    print("YES")        