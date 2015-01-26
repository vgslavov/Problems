# examples
reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
reverse_words('double  spaced  words') # 'elboud  decaps  sdrow'

# my solution
import re
def reverse_words(str):
    return ''.join([w[::-1] for w in re.split("(\S+)", str)])

# my solution (doesn't work on: multiple spaces)
def reverse_words(str):
    return ' '.join([w[::-1] for w in str.split()])

# my solution (doesn't work on: punctuation)
import re
def reverse_words(str):
    return ''.join([w[::-1] for w in re.split("(\W+)", str)])
