# find largest element <= x
# O(log n)
def bin_search(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while (beg <= end):
        mid = (beg + end) / 2
        if (A[mid] <= x):
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
