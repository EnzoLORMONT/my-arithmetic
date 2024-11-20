# my_arithmetic_$USER/gcd.py

def gcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers."""
    while b:
        a, b = b, a % b
    return abs(a)
