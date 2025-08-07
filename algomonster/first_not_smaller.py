#!/usr/bin/env python3

# tags: binary search

def feasible(num, target):
    return num >= target
    
def first_not_smaller(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    first = -1

    while left <= right:
        mid = (left+right) // 2

        if feasible(arr[mid], target):
            first = mid
            right = mid-1
        else:
            left = mid+1
            
    return first

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)