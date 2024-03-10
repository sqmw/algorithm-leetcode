#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
求Sn=1!+2!+3!+4!+5!+…+n!之值，其中n是一个数字(n不超过20)。
"""
import math


def factorial(n: int) -> int:
    des_sum: int = 0

    now_factorial = 1
    for i in range(1, n + 1):
        now_factorial *= i
        des_sum += now_factorial

    return des_sum


if __name__ == "__main__":
    print(math.pow(1200, 3))
