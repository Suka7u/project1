def one(n) -> int:
    """
    Returns the sum of every number from 1 to n
    :param n: A number to set the range
    :return: The sum
    """
    check(n)
    if n == 1:
        return 1
    else:
        return n + one(n-1)


def two(num, exp) -> int:
    """
    Calculates power
    :param num: A number as a base
    :param exp: The exponent to the number
    :return: The result of the calculation
    """
    check(num, exp)
    if exp == 1:
        return num
    else:
        return num * two(num, exp - 1)


def three(n) -> str:
    """
    Returns numbers from n - 1
    :param n: A number to set the range
    :return: The string of numbers from n - 1
    """
    check(n)
    if n == 1:
        return 1
    else:
        return f'{n} {three(n-1)}'


def four(n1, n2) -> int:
    """
    Calculates the sum of sums
    :param n1: The smallest number
    :param n2: The largest number
    :return: The sum of the sums of the numbers n1 - n2 from nx - 1
    """
    a = 0
    check(n1, n2)
    while n2 >= n1:
        a += one(n2)
        n2 -= 1
    return a


def check(*args) -> None:
    """
    Checks whether input is a string
    :param args: each number to check
    :return: none
    """
    for x in args:
        if type(x) != int:
            raise ValueError('Data Type')
        if x <= 0:
            raise ValueError('Negative')