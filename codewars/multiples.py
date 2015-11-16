# example
# If we list all the natural numbers below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# my solution: generator expression
def solution(number):
    return sum((i for i in xrange(number) if i % 3 == 0 or i % 5 == 0))

# my solution: list comprehension (slower)
def solution(number):
    return sum([i for i in xrange(number) if i % 3 == 0 or i % 5 == 0])

# my solution: bad code
def solution(number):
    sum = 0
    for i in xrange(number):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum

# others: best!
def solution(number):
    return sum(set(list(range(0, number, 3)) + list(range(0, number, 5))))
