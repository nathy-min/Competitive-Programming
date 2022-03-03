import math as mt
def domino():
    m, n = map(int, input().split())
    return(mt.floor(m*n/2))
print(domino())
