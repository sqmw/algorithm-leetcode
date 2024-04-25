import time
from functools import cache


def slow_fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


@cache
def slow_fib_with_cache(n: int) -> int:
    if n <= 1:
        return n
    else:
        return slow_fib_with_cache(n - 1) + slow_fib_with_cache(n - 2)


if __name__ == '__main__':
    print(int(1.2))
