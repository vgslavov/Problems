#!/usr/bin/env python3

# tags: binary search

# complexity:
# run-time: O(log n)
# space: O(1)
def find_min_rotated(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left) // 2

        # rotation is to the right
        if arr[mid] > arr[-1]:
            left = mid+1
        elif mid > 0 and mid < len(arr)-1 and arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
            return mid
        else:
            right = mid-1
            
    return mid

# solution: follow pattern
# complexity:
# run-time: O(log n)
# space: O(1)
def find_min_rotated2(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = 0

    while left <= right:
        mid = left + (right-left) // 2

        # min is to the left
        if arr[mid] <= arr[-1]:
            # record first not larger
            boundary = mid
            right = mid-1
        else:
            left = mid+1
            
    return boundary

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = find_min_rotated2(arr)
    print(res)