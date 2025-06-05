from functools import lru_cache


def fibo(n: int=10) -> int:
    """Returns nth number of the Fibonacci series starting with 0
    
    Argument:
    - n[int]: number of elements to compute in the Fibonacci series
    (min value = 1, default value = 10)

    Returns [int]: the nth number

    Raises: ValueError if n <= 0
    """
    if n <= 0:
        raise ValueError("argument must be strictly positive")
    v1 = 0
    v2 = 1
    if n == 1:
        return v1
    elif n == 2:
        return v2
    else:
        for _ in range(n - 2):
            v3 = v1 + v2
            v1 = v2
            v2 = v3
        return v3

@lru_cache
def fibo_rec(n: int=10) -> int:
    """Returns nth number of the Fibonacci series starting with 0
    
    Argument:
    - n[int]: number of elements to compute in the Fibonacci series
    (min value = 1, default value = 10)

    Returns [int]: the nth number

    Raises: ValueError if n <= 0
    """
    if n <= 0:
        raise ValueError("argument must be strictly positive")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)
    
def fibo_list(n: int=10) -> list[int]:
    """Returns the nth first numbers of the Fibonacci series starting with 0
    
    Argument:
    - n[int]: number of elements to compute in the Fibonacci series
    (default value = 10)

    Returns [int]: the series with n values

    NB: if n <=0, the empty list is returned
    """
    pass


if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    value = fibo_rec(n)
    print(f"The {n}th value of Fibonacci series is {value}")
    print("The 10th value of Fibonacci series is",  fibo())

    