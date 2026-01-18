# examples
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"

# my solution
def divisors(integer):
    div = []
    for d in range(2, integer):
        if not integer % d:
            div.append(d)

    if not div:
        return "{n} is prime".format(n=integer)

    return div

# others
divisors = lambda z: [i for i in range(2,z) if z % i == 0] or ("%d is prime" % z)

def divisors(integer):
    return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

