#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                m = arr[j + 1]
                arr[j + 1] = arr[j]
                print(" ".join(list(map(str,arr))))
                arr[j] = m
    print(" ".join(list(map(str,arr))))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
