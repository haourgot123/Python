from math import *

f = [1] * (10 ** 6 + 1)

def sangnto():
    f[0] = 0
    f[1] = 0
    for i in range(2, isqrt(10 ** 6) + 1):
        if f[i] == 1:
            for j in range(i * i, 10 ** 6 + 1, i):
                f[j] = 0
    
            



if __name__ == "__main__":
    sangnto()
    F = [0] * (10 ** 6 + 1)
    F[0] = 0
    F[1] = 0
    for i in range(2, 10 ** 6 + 1):
        F[i] = F[i - 1] + f[i]
    t = int(input())
    while t > 0:
        n = int(input())
        print(F[n])        
        t -= 1