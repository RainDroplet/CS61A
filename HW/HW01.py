from operator import add, sub, mul

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

    if b < 0:
        # if b is negative then f needs to be subtraction
        f = sub(a,b)
    else:
        # all else chances are going to be the b variable is a positive
        f = add(a,b)

    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    if a >= b >= c:
        # this will check if a and b are both bigger than c
        return add(mul(a,a),mul(b,b))
    elif b >= c >= a:
        # this will check if b and c are bigger than a
        return add(mul(c,c),mul(b,b))
    else:
        # all else will result that c and a are the biggest
        return add(mul(c,c),mul(a,a))

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """