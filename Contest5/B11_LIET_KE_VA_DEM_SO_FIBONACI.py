`    from math import *

    def check(n):
        if n == 0 or n == 1:
            return True
        f0 = 0
        f1 = 1
        for i in range(2, 150):
            fn = f0 + f1
            if fn >  n:
                return False
            if fn == n:
                return True
            f0 = f1
            f1 = fn


    if __name__ == "__main__":
        n = int(input())
        a = list(map(int, input().split()))
        dem  = 1
        for i in range(len(a)):
            if check(a[i]):
                print(a[i], end = " ")
                dem = 0
        if dem:
            print("NONE")
        