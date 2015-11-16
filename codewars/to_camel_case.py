# examples
# "the-stealth-warrior" -> "theStealthWarrior"
# "The_Stealth_Warrior" -> "theStealthWarrior"
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not
        returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior",
"to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior",
"to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did
not return correct value")

# my solution
import re
def to_camel_case(text):
    camel = ''.join([w.capitalize() for w in re.split("([a-zA-Z][^-_]*)",
                        str(text)) if w not in ('', '-', '_')])
    if not text:
        return text

    if not text[0].isupper():
        return camel[:1].lower() + camel[1:]

    return camel

# others
def to_camel_case(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in
        text.replace("_", "-").split("-")])[1:] if text else ''

import re
def to_camel_case(text):
    return reduce(lambda p, n: p + n[0].upper() + n[1:], re.split('[-_]',
        text))

from re import compile as reCompile
PATTERN = reCompile(r'(?i)[-_]([a-z])')
def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)

import re

def to_camel_case(text):
    words = re.split(r'[_\-]', text)
    return ''.join([words[0]] + [word.capitalize() for word in
        words[1:]])
