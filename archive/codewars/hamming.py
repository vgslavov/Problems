# examples
hamming("I like turtles","I like turkeys")  //returns 3
hamming("Hello World","Hello World")  //returns 0

# my solution
def hamming(a,b):
    return len([i for i, j in zip(a, b) if i != j])

# my solution (old)
def hamming(a,b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

# others
def hamming(a,b):
    return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))
