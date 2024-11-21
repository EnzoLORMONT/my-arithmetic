# my_arithmetic_$USER/gcd.py

def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two numbers.

    Parameters
    ----------
    a : int
        First number.
    b : int
        Second number.

    Returns
    -------
    int
        The greatest common divisor of `a` and `b`.
    """
    while b:
        a, b = b, a % b
    return abs(a)
