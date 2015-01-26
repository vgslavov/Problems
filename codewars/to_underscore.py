# examples

# my solutions
import re
def to_underscore(string):
    return '_'.join(w.lower() for w in re.split("([A-Z][^A-Z]*)",
        str(string)) if w)

# fails on: numbers only (4)
import re
def to_underscore(string):
    return '_'.join(w.lower() for w in re.findall('[A-Z][a-z]*\d*',
        str(string)))

# others
import re
def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()
