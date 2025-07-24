#!/usr/bin/env python3

import sys
import unittest

# number: 394
# title: Decode String
# url: https://leetcode.com/problems/decode-string/
# difficulty: medium
# tags: stack, string

# constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

# non-solution: stack
# complexity:
# run-time: O(n)
# space: O(n)
# TODO: fix bugs
def decode_str(s: str) -> str:
    num = 0
    substr = ''
    # element: (num, substr)
    stack = []

    for c in s:
        # char
        if c.isalpha():
            substr += c
        # multi-digit num
        elif c.isdigit():
            # edge case: a2
            if substr:
                stack.append((1,substr))
                substr = ''
            # build number digit-by-digit
            num = (num * 10) + ord(c) - ord('0')
        # push to stack: (count, '')
        elif c == '[':
            stack.append((num, ''))
            num = 0
        # pop from stack
        elif c == ']':
            if stack and stack[-1][1]:
                stack.append((1,substr))
            else:
                n,_ = stack.pop()
                stack.append((n,substr))
            substr = ''
        else:
            print(f"invalid input: {c}")

    #print(f"stack:{stack}")

    pre_ans = []
    ans = []

    # iterate over stack
    while len(stack):
        n, s = stack.pop()
        if not s:
            if n == 1 and pre_ans:
                ans.append(pre_ans.pop())
            else:
                pre_ans *= n
        else:
            pre_ans.append(n*s)

        #print(f"ans:{ans}")
        #print(f"pre_ans:{pre_ans}")

    ans.extend(pre_ans)
    ans.reverse()
    ans.append(substr)

    return ''.join(ans)

# solution: Leetcode 2 stacks
# complexity:
# run-time: O(n)
# space: O(n)
def decode_str2(s: str) -> str:
    count_stack = []
    str_stack = []
    ans = ''
    num = 0

    # example: 3[a]2[bc]
    # 3: num = 3
    # [: count_stack = [3], num = 0
    # a: ans = 'a'
    # ]: ans = 3 * 'a' = 'aaa', count_stack = [], ans = ''
    # 2: num = 2
    # [: count_stack = [2], str_stack = ['aaa']
    # b: ans = 'b'
    # c: ans = 'bc'
    # ]: ans = 'aaa' + 2 * 'bc' = 'aaabcbc'
    for c in s:
        # read number digit-by-digit
        if c.isdigit():
            num = (num*10) + ord(c) - ord('0')
        # push to both stacks
        elif c == '[':
            # count stack: last count
            count_stack.append(num)
            # string stack: current ans
            str_stack.append(ans)
            num = 0
            ans = ''
        # build substr
        elif c.isalpha():
            ans += c
        # decode
        elif c == ']':
            # current ans + latest decoded string
            ans = str_stack.pop() + count_stack.pop() * ans
        else:
            print(f"invalid char: {c}")

        #print(f"ans: {ans}")
        #print(f"count_stack: {count_stack}")
        #print(f"str_stack: {str_stack}")

    return ans

class TestDecodeStr(unittest.TestCase):
    def test_decode_str(self):
        self.assertEqual(decode_str("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decode_str2("3[a]2[bc]"), "aaabcbc")

        self.assertEqual(decode_str("3[a2[c]]"), "accaccacc")
        self.assertEqual(decode_str2("3[a2[c]]"), "accaccacc")

        self.assertEqual(decode_str("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(decode_str2("2[abc]3[cd]ef"), "abcabccdcdcdef")

        self.assertEqual(decode_str("abc3[cd]xyz"), "abccdcdcdxyz")
        self.assertEqual(decode_str2("abc3[cd]xyz"), "abccdcdcdxyz")

        self.assertEqual(decode_str("2[3[a]b]"), "aaabaaab")
        self.assertEqual(decode_str2("2[3[a]b]"), "aaabaaab")

        self.assertEqual(decode_str("10[a]"), "aaaaaaaaaa")
        self.assertEqual(decode_str2("10[a]"), "aaaaaaaaaa")

        self.assertEqual(decode_str("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"), "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
        self.assertEqual(decode_str2("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"), "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")

        self.assertEqual(decode_str("2[ab3[cd]]4[xy]"), "abcdcdcdabcdcdcdxyxyxyxy")
        self.assertEqual(decode_str2("2[ab3[cd]]4[xy]"), "abcdcdcdabcdcdcdxyxyxyxy")

        # TODO: fix bugs
        #self.assertEqual(decode_str("2[20[bc]31[xy]]xd4[rt]"), "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxybcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxdrtrtrtrt")
        self.assertEqual(decode_str2("2[20[bc]31[xy]]xd4[rt]"), "bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxybcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxdrtrtrtrt")

if __name__ == "__main__":
    sys.exit(unittest.main())
