from math import *

def print_list1(a, left, right):
    if left > right:
        return
    else:
        print(a[left], end = " ")
        print_list1(a,left + 1, right)
         
def print_list2(a, left, right):
    if left > right:
        return
    else:
        print(a[right], end = " ")
        print_list2(a,left, right - 1) 



if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print_list1(a,0, n - 1)
    print()
    print_list2(a,0,n - 1)