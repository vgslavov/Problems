# examples
# for i from 1 to n, do i % m and return the sum
# f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)

# my solution: generator expression
# too long
def f(n, m):
    end = int(n+1)
    return sum((i % m for i in xrange(end)))

# my solution: generator expression
# TypeError: range() integer end argument expected, got float.
def f(n, m):
    return sum(i % m for i in xrange(n+1))

# my solution: list comprehension
def f(n, m):
    return sum([i % m for i in xrange(n+1)])
