""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import math
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        T(n): O(n ** 1.5)
        S(n): O(n)
        使用动态规划
        """

        rec_f: List[int] = [i for i in range(n + 1)]

        for i in range(4, n + 1):
            cou_min = float('inf')
            if i == int(math.pow(i, 0.5)) ** 2:
                cou_min = 1
            else:
                t = int(math.pow(i, 0.5))
                # 这里的时间复杂度是 O(n**0.5)
                # for j in range(t, 1, -1):
                # for j in range(t, int(math.pow((i - 1) // 2, 0.5)), -1):
                for j in range(t, max(int(math.pow((i - 1) // 2, 0.5)) - 5, 1), -1):
                    product = j * j
                    cou_min = min(cou_min, rec_f[product] + rec_f[i - product])
            rec_f[i] = cou_min
        # print(rec_f)
        return rec_f[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(5))
