#!/usr/bin/env python3

def find_boundary(arr: list[bool]) -> int:
    left = 0
    right = len(arr)-1

    # no equality
    while left < right:
        mid = left + (right-left)//2

        # if False, go right
        if not arr[mid]:
            left = mid+1
        else:
            right = mid

    if left < len(arr) and arr[left]:
        return left
        
    return -1

def feasible(arr: list[int], i: int) -> bool:
    return arr[i] == True

# more generic
def find_boundary2(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1

    # preserve equality
    while left <= right:
        mid = (left + right) // 2

        if feasible(arr, mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index

if __name__ == "__main__":
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)