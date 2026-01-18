# examples
Test.assert_equals(abbreviate("internationalization"), "i18n")
Test.assert_equals(abbreviate("accessibility"), "a11y")
Test.assert_equals(abbreviate("Accessibility"), "A11y")

# my solution 3
import re
def abbreviate(s):
    abbr = []
    for w in re.split('(\W+)', s):
        if len(w) >= 4:
            w = ''.join([w[0], str(len(w)-2), w[-1]])
        abbr.append(w)
    return ''.join(abbr)

# my solution 2
# fails on: 'balloon, monolithic.'
import string
def abbreviate(s):
    abbr = []
    for phrase in s.split():
        for word in phrase.strip().split('-'):
            if len(word) > 4:
                word = ''.join([word[0], str(len(word)-2), word[-1]])
            abbr.append(word)
    return '-'.join(abbr)

# my solution 1
# fails on: 'balloon, monolithic.'
def abbreviate(s):
    abbr = []
    for w in s.split('-'):
        if len(w) > 4:
            w = ''.join([w[0],str(len(w)-2),w[-1]])
        abbr.append(w)
    return '-'.join(abbr)

# others
import re
def abbreviate(s):
    ab = lambda w: w[:1] + str(len(w) - 2) + w[-1:]
    return re.sub(r'\w{4,}', lambda m: ab(m.group(0)), s)

abbreviate=lambda s:__import__('re').sub('\w{4,}',lambda m:(lambda
    w:w[0]+str(len(w)-2)+w[-1])(m.group(0)),s)

import re
regex = re.compile('[a-z]{4,}', re.IGNORECASE)
def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]
def abbreviate(s):
    return regex.sub(replace, s)
