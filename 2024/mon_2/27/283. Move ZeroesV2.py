""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        T(n): O(n)
        S(n): O(1)
        """
        left_add: int = 0
        right_select: int = 0
        while right_select < len(nums):
            if nums[right_select] != 0:
                nums[left_add], nums[right_select] = nums[right_select], nums[left_add]
                left_add += 1
            right_select += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
    ...
