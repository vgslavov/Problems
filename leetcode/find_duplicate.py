#!/usr/bin/env python

import sys

def set_bit(value, bit_index):
    return value | (1 << bit_index)

def get_bit(value, bit_index):
    return value & (1 << bit_index)

def find_duplicate(nums):
    bitmap = 0
    for num in nums:
        print("{}:{}:{}".format(num, bin(num), bin(bitmap)))
        if get_bit(bitmap, num):
            return num
        else:
            bitmap = set_bit(bitmap, num)

def main():
    nums = [1,5,1,3,1,4]
    print("nums:{}".format(nums))
    print("duplicate:{}".format(find_duplicate(nums)))

if __name__ == '__main__':
    sys.exit(main())
