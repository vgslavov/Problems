# examples
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabbcdeB" -> 2 # 'a' and 'b'
# "indivisibility" -> 1 # 'i'
# "Indivisibilities" -> 2 # 'i' and 's'

# my solution
from collections import Counter
def duplicate_count(text):
    return len([(k, v) for k, v in Counter(text.lower()).items() if v > 1])

# others
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# doesn't work on 3
from collections import Counter
def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)

from collections import Counter
def duplicate_count(text):
    return sum(n > 1 for n in Counter(text.upper()).itervalues())

def duplicate_count(text):
    text = text.lower()
    return len([x for x in set(text) if text.find(x) != text.rfind(x)])
