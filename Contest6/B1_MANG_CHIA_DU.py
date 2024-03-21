from math import *

f = [1] * (10 ** 6 + 1)
MOD = 10 ** 9 + 7

def init():
    f[0] = 1
    for i in range(1, 10 ** 6 + 1):
        f[i] = i * f[i - 1] % MOD
        f[i] %= MOD

if __name__ == "__main__":
    t =int(input())
    init()
    while  t > 0:
        n = int(input()) 
        print(f[n])
        t -= 1
        
           