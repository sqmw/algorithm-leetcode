import sys


def slow_fib(n: int):
    if n <= 1:
        return n
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


if __name__ == "__main__":
    print(sys.maxsize)
    print(sys.maxsize + sys.maxsize)
