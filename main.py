import time


def slow_fib(n: int):
    if n <= 1:
        return n
    else:
        return slow_fib(n - 1) + slow_fib(n - 2)


if __name__ == "__main__":
    t = time.time()
    print(slow_fib(45))
    print(time.time() - t)
