from math import *


def check(a,left, right):
    if left > right:
        return True
    else:
        if a[left] % 2 == 1:
            return False
        else:
            return check(a,left + 1, right)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    if check(a, 0, n - 1):
        print("YES")
    else:
        print("NO")