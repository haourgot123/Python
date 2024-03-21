from math import *



def cnt_digit(n):
    if n < 10:
        return 1
    return 1  + cnt_digit(n // 10)


if __name__ == "__main__":
    n = int(input())
    ans = cnt_digit(n)
    print(ans)