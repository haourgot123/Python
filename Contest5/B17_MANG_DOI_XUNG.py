from math import *


        
        


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(len(a)):
        b.append(a[i])
    b.reverse()
    if a == b:
        print("YES")
    else:
        print("NO")