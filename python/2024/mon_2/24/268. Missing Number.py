""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        思路：可以按照梯形的面积求出没有去掉数字时候的sum0
             sum0 - sum(nums) == val_missing
        """
        height = len(nums) + 1
        a = 0
        b = len(nums)
        return ((a + b) * height) // 2 - sum(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(s.missingNumber(nums))
