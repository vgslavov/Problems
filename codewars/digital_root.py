# examples
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

# my solution
def digital_root(n):
    while len(map(int, str(n))) > 1:
        n = sum(map(int, str(n)))
    return n

# others
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
    return n if n < 10 else digital_root(sum([int(d) for d in str(n)]))

# TODO: understand
def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0

def digital_root(n):
    while n > 9:
        n = sum([int(i) for i in str(n)])
    return n
