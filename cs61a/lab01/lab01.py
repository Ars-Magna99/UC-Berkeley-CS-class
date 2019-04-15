"""Lab 1: Expressions and Control Structures"""
# Ziyang Wang 2019-04-14
# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    assert n > 0, 'n must be positive'
    time = 0
    while time < n:
        time += 1
        x = f(x)
    return x

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    int_len = len(str(n))
    digit_list = []
    for i in range(0,int_len):
        digit_list.append(n % 10)
        n = n // 10
    print (digit_list)
    return sum(digit_list)



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """

    """
    int_len = len(str(n))
    digit_list = []
    location_list = []
    if n == 8:
        return False

    for i in range(0,int_len): #extract all digits
        digit_list.append(n % 10)
        n = n // 10

    for j in range(0,len(digit_list)): #find all the 8 
        if digit_list[j] == 8:
            location_list.append(j)
    print (location_list)
    """
    while n > 0:
        remainder = n % 10
        n = n // 10
        if remainder == 8:
            if n % 10 == 8:
                return True
            else:
                remainder, n = n % 10, n // 10
        return False



