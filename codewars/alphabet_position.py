# examples
test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."),
"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."),
"20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

# my solution
import string
def alphabet_position(text):
    position = {}
    for n,l in enumerate(string.lowercase, 1):
        position[l] = str(n)
    return ' '.join([position[c] for c in text.lower() if c.isalpha()])

# others
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

import string
def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower())+1) for
        letter in list(text) if letter.isalpha()])

import string
def alphabet_position(text):
    text = text.lower().strip()
    return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in
        string.ascii_letters] )
