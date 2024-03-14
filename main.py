#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
求Sn=1!+2!+3!+4!+5!+…+n!之值，其中n是一个数字(n不超过20)。
"""
import heapq
import math

cou = 0


def foo(n: int):
    global cou
    cou += 1
    if n <= 3:
        return 1
    else:
        return foo(n - 3) + foo(n - 5)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 9, 6, 7]
    heapq.heapify(l)
    for _ in range(len(l)):
        print(heapq.heappop(l))
