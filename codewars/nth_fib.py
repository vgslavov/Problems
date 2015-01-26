# examples
nth_fib(4) == 2

# my solution
def nth_fib(n):
    for i, f in enumerate(fib(), 1):
        if i == n:
            return f

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a+b

# others
def nth_fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

# slow?
def nth_fib(n):
    if n <= 2:
        return n-1
    return nth_fib(n-1) + nth_fib(n-2)
