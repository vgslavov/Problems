# examples
sumDigits(10)  # Returns 1
sumDigits(99)  # Returns 18
sumDigits(-32) # Returns 5

# my solution
def sumDigits(number):
    sum = 0
    if number < 0:
        number *= -1
    while number > 0:
        sum += (number % 10)
        number /= 10
    return sum

# others
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))

def sumDigits(number):
    return sum(map(int, str(abs(number))))
