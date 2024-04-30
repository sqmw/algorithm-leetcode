#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        method2: 两边进行遍历，不使用除法
        T(n): O(n)
        S(n): O(n)
        """
        des_list: List[int] = [1] * len(nums)

        # 左乘
        product = nums[0]
        for i in range(1, len(nums)):
            des_list[i] = product
            product *= nums[i]
        product = nums[len(nums) - 1]
        # 右乘
        for i in range(len(nums) - 2, -1, -1):
            des_list[i] *= product
            product *= nums[i]

        return des_list


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([0, 0, 1, 2, 3]))
