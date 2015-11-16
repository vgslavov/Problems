# examples
# ['n', 's', 'w', 'e']

# my solution (correct)
def isValidWalk(walk):
    return len(walk) == 10

# others: why?
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and
        walk.count('e') == walk.count('w')
