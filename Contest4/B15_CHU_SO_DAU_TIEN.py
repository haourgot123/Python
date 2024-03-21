from math import *

def first_digit(n):
    if n < 10:
        return n
    return first_digit(n // 10)
    



if __name__ == "__main__":
    n = int(input())
    ans = first_digit(n)
    print(ans)