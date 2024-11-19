#!/usr/bin/env python3

def print_fibonacci(length):
    if (length == 0):
        print([])
        return []
    if (length == 1): 
        print([0])
        return [0]
    resultArr = [0, 1]
    for n in range(2, length): 
        resultArr.append(resultArr[n - 2] + resultArr[n - 1])
    print(resultArr)
    return resultArr