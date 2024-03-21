from math import*




if __name__ == "__main__":
    a,b = map(int, input().split())
    x = ceil(sqrt(a))
    y = isqrt(b)
    print(y - x + 1)