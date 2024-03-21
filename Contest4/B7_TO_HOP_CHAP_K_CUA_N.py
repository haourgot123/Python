from math import *

def C(n,k):
    if k == 0 or k == n:
        return 1
    return C(n-1,k-1) + C(n-1,k)


if __name__ == "__main__":
    n,k = map(int, input().split())
    ans = C(n,k)
    print(ans)