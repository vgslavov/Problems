# examples
spread(somefunc, [1, True, "foo"])
# to be same as
somefunc(1, True, "foo")

# my solution
def spread(func, args):
    return func(*args)

# others

spread=apply

spread = lambda func, args: func(*args)
