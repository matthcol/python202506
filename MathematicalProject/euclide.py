# module euclide
# https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide

def pgcd(a: int, b: int) -> int:
    """Greatest common divisor of natural integers a and b
    
    Arguments:
    - a [int]: must be strictly positive
    - b [int]: must be strictly positive

    Returns [int]: greatest common divisor
    """
    if a <=0 or b <= 0:
        raise ValueError("argument must be stricly positive")
    while a!=b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a