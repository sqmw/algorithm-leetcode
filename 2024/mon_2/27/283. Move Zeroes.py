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
        T(n): O(cou_zero * n)
        S(n): O(1)
        
        下面通过删除添加实现的，实际也可以直接通过移动元素的位置实现
        """
        now_zero_index = len(nums)
        for i in range(now_zero_index - 1, -1, -1):
            if nums[i] != 0:
                break
            else:
                now_zero_index -= 1
        i = 0
        while i < now_zero_index:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                now_zero_index -= 1
            else:
                i += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
    ...
