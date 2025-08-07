#!/usr/bin/env python3

# tags: binary search

# non-solution: buggy if peak is at index 0 or len(arr)-1
# complexity:
# run-time: O(log n)
# space: O(1)
def peak_of_mountain_array(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left) // 2

        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid] and arr[mid] < arr[mid+1]:
            left = mid+1
        else:
            right = mid-1

    return 0

# solution: follow pattern
# complexity:
# run-time: O(log n)
# space: O(1)
def peak_of_mountain_array2(arr: list[int]) -> int:
    left = 0
    right = len(arr)-1
    boundary = 0

    while left <= right:
        mid = left + (right-left) // 2

        # found peak or it's to left
        if arr[mid] > arr[mid+1]:
            boundary = mid
            right = mid-1
        else:
            left = mid+1

    return boundary

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array2(arr)
    print(res)