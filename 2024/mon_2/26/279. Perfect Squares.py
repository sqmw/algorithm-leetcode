""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import math
from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        严重超时
        """
        num_cou = 0
        des_arr: List[int] = []

        def recurse_get_des(val_need: int):
            nonlocal num_cou
            nonlocal des_arr
            if val_need == 0:
                des_arr.append(num_cou)
            t = int(math.pow(val_need, 0.5))
            for i in range(t, 0, -1):
                num_cou += 1
                recurse_get_des(val_need - i * i)
                num_cou -= 1

        recurse_get_des(n)

        return min(des_arr)


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(40))
