# examples
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox')

# my solution
def title_case(title, minor_words=None):
    if minor_words:
        exclude = minor_words.lower().split()
    else:
        exclude = []
    words = title.lower().split()

    if len(words) >= 1:
        title_c = words[0].capitalize()
    else:
        return ''

    for w in words[1:]:
        if w in exclude:
            mod = w.lower()
        else:
            mod = w.capitalize()
        title_c = ' '.join([title_c, mod])

    return title_c

# others
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for
        word in title])

def title_case(title, minor_words=""):
    # title.capitalize():
    # capitalizes only the first char of title and lowers everything else
    return " ".join([w if w in minor_words.lower().split() else
        w.capitalize() for w in title.capitalize().split()])
