from math import *





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    cnt = 1
    docung = a[0]
    for i in range(1, n):
        if docung <= 0:
            break
        else:
            cnt += 1
        docung = min(docung - 1, a[i])
    
    print(cnt)