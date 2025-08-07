#!/usr/bin/env python3

# tags: binary search

def square_root(n: int) -> int:
    if not n:
        return 0

    left = 1
    right = n
    ans = 0

    while left <= right:
        mid = left + (right-left) // 2
        squared = mid * mid
        
        if squared == n:
            return mid
        elif squared > n:
            # record first not smaller
            ans = mid
            right = mid-1
        else:
            left = mid+1
            
    # square root is b/w ans and ans-1
    return ans-1

if __name__ == "__main__":
    n = int(input())
    res = square_root(n)
    print(res)