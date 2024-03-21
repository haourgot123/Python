from math import*

def check(n):
    if n < 10:
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        if n % 2 == 1: return False
        else: return check(n // 10)
            



if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")