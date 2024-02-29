""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List, Set


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        正常的整数序列 [1,2,3,...] 即 index + 1 = val
        """

        if max(nums) <= 0:
            return 1
        for i in range(len(nums)):
            while 0 < nums[i] < len(nums) + 1 and i + 1 != nums[i] and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,1]))
