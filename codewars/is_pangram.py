# examples
pangram = "The quick, brown fox jumps over the lazy dog!"

# my solution
from collections import defaultdict
def is_pangram(s):
    letters = defaultdict(int)

    for l in s:
        if l.isalpha():
            letters[l.lower()] += 1

    return len(letters) == 26

# others
# problem: a lot of non-alpha chars?
import string
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

import string
def is_pangram(s):
    #for l in string.ascii_lowercase:
    for l in string.lowercase:
        if l not in s.lower():
            return False
    return True

import string
def is_pangram(s):
    s = s.lower()
    # true if bool true for all iterables
    return all(letter in s for letter in string.lowercase)
