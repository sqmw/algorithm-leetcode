#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        method1: 分类讨论思想
        T(n): O(n)
        S(n): O(n)
        """
        des_list: List[int] = [0] * len(nums)

        no_zero_product = 1
        zero_cou: int = 0
        for num in nums:
            if num != 0:
                no_zero_product *= num
            else:
                zero_cou += 1
        if zero_cou > 1:
            return des_list
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_cou == 1:
                    des_list[i] = no_zero_product
                else:
                    des_list[i] = 0
            else:
                if zero_cou == 0:
                    des_list[i] = no_zero_product // nums[i]
                else:
                    des_list[i] = 0

        return des_list


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([0, 0, 1, 2, 3]))
