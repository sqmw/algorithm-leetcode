""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List, Set


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        """
        if max(nums) <= 0:
            return 1
        nums_set: Set = set(nums)
        for i in range(1, max(nums_set) + 2):
            if i not in nums_set:
                return i


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))
