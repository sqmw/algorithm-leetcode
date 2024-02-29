""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 四平方和定理：任何一个正整数都可以表示为不超过四个整数的平方之和
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        if (int(math.pow(n, 0.5)) ** 2) == n:
            return 1
        a = 0
        while a * a <= n:
            b = int((n - a * a) ** 0.5)
            if a * a + b * b == n:
                return 2
            a += 1
        return 3


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(11))
