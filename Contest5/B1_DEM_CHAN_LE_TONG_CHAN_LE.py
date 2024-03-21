from math import *





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    sole = 0
    sochan = 0
    sum_le = 0
    sum_chan = 0
    for i in range(len(a)):
        if  a[i]  % 2 == 0:
            sochan += 1
            sum_chan += a[i]
        else:
            sole += 1
            sum_le += a[i]
    print(sochan)
    print(sole)
    print(sum_chan)
    print(sum_le)