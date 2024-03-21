from math import *




if __name__ == "__main__":

    a = []
    for i in range(0, n):
        x = list(map(int, input().split()))
        a += x
    chan  = 0
    le = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            chan += 1
        else:
            le += 1
    if chan > le:
        print("CHAN")
    elif le > chan:
        print("LE")
    else:
        print("CHANLE")          
            
        