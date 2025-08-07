#!/usr/bin/env python3

# tags: binary search

# complexity:
# run-time: O(log n)
# space: O(1)
def find_first_occurrence(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr)-1
    first = -1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            first = mid
            right = mid-1
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    
    return first

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)