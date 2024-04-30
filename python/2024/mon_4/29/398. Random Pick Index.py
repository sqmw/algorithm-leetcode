import collections
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        # 初始化 indexes 数组
        # 遍历得到数组
        """
        T(n): O(n)
        S(n): O(n) # 因为 hash 存储了每一个下表，以及每一个不同的数字，主要的内存来自不同的下标
        """
        self._val_dic_arr = collections.defaultdict(list)
        self._ini_arr = nums
        for i in range(len(nums)):
            self._val_dic_arr[nums[i]].append(i)

    def pick(self, target: int) -> int:
        """
        T(n): O(1)
`       S(n): O(1)
        """
        _val_indexes_arr_select: List[int] = self._val_dic_arr[target]
        _val_indexes_arr_index_select = random.randint(0, len(_val_indexes_arr_select) - 1)
        _target_ini_arr_index = _val_indexes_arr_select[_val_indexes_arr_index_select]
        return _target_ini_arr_index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
