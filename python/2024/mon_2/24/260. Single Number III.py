""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import collections
from typing import List, Dict


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        T(n): O(n)
        S(n): O(n)
        理解题目：从题目知道数字出现的次数仅仅1或者2并且出现一次的仅仅两个
        实现思路：使用dict实现，出现一次记一次，然后返回出现一次的
        """
        des_nums: List[int] = []
        num_dic: Dict = collections.defaultdict(lambda: 0)
        for item in nums:
            num_dic[item] += 1
        for item in nums:
            if num_dic[item] == 1:
                des_nums.append(item)
        return des_nums


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    print(s.singleNumber(nums))
