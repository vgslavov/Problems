#!/usr/bin/python

def greedyCoinChanging(M, k):
    n = len(M)
    result = []
    print("iter,result,k")
    for i in xrange(n - 1, -1, -1):
        result += [(M[i], k // M[i])]
        k %= M[i]
        print(i, result, k)

    return result

M = [1,5,25]
k = 35
print("M:",M)
print("k:",k)
result = greedyCoinChanging(M, k)
print(result)

if __name__ == 'main':
    main()
