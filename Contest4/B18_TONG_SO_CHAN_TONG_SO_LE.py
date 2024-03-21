from math import *

def sum_odd(n):
    if n < 10:
        if n %  2 == 1:
            return n
        else:
            return 0
    else:
        if n % 2 == 1:
            return n % 10 + sum_odd(n // 10)
        else:
            return sum_odd(n // 10)

def sum_even(n):
    if n < 10:
        if n %  2 == 0:
            return n
        else:
            return 0
    else:
        if n % 2 == 0:
            return n % 10 + sum_even(n // 10)
        else:
            return sum_even(n // 10)

if __name__ == "__main__":
    n = int(input())
    ans1 = sum_odd(n)
    ans2 = sum_even(n)
    print(ans2)
    print(ans1)