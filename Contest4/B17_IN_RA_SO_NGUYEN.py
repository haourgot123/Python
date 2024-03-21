from math import *



def print_left_to_right(n):
    if n == 0:
        return
    print(n % 10, end = " ") 
    return print_left_to_right(n // 10)     

def print_right_to_left(n):
    if n == 0:
        return
    print_right_to_left(n // 10)
    print(n % 10, end = " ")


if __name__ == "__main__":
    n = int(input())
    print_right_to_left(n)
    print()
    print_left_to_right(n)