
from math import *

f = [0] * (10 ** 6 + 1)
MOD  = 10 ** 9 + 7

def init():
    f[0] = 0
    f[1] = 1
    for i in range(2,10 ** 6 + 1):
        f[i] = f[i - 1] + f[i - 2]
        f[i] %= MOD

if __name__ == "__main__":
    t  = int(input())
    init()
    while t > 0:
        n = int(input())
        print(f[n])
        t -=1