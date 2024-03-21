from math import *

def sum_digit(n):
    if n < 10:
        return n
    return n % 10 + sum_digit(n // 10)
        



if __name__ == "__main__":
    n = int(input())
    ans = sum_digit(n)
    print(ans)
    