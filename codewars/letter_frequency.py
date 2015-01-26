# examples

# my solution
from operator import itemgetter
from collections import Counter
def letter_frequency(text):
    return sorted([(k, v) for k, v in sorted(Counter(text.lower()).items(),
        key=itemgetter(0)) if k.isalpha()], key=itemgetter(1), reverse=True)

# others
from collections import Counter
from operator import itemgetter

def letter_frequency(text):
    items = Counter(c for c in text.lower() if c.isalpha()).items()
    return sorted(
        sorted(items, key=itemgetter(0)),
        key=itemgetter(1),
        reverse=True

from collections import Counter
def letter_frequency(text):
  return sorted(Counter(filter(str.isalpha, text.lower())).most_common(),
      key=lambda t:(-t[1],t[0]))
