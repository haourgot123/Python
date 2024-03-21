from math import *

def csln(n):
    if n < 10:
        return max(0, n)
    return max(n % 10, csln(n // 10) % 10)

def csnn(n):
    if n < 10:
        return min(10, n)
    return min(n % 10, csnn(n // 10) % 10)
    

if __name__ == "__main__":
    n = int(input())
    ans = csln(n)
    res = csnn(n)
    print(ans, res)