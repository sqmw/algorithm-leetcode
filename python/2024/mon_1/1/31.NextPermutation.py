"""
考察数学思维，递推、递归、进位
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 越往后大的数字越往前
        # 本质是递归或者归纳思想、进位思想，从后往前看，有序就继续往前看，直到next小于当前的值
        # 继续上面，直到next更小之后，从后往前看到next的前一个数字，找到第一个大于 next 的数
        # 和next对应的数字进行交换，然后将从 next 下一个到数组结尾的部分进行升序排列，得到的就是结果
        """
        Do not return anything, modify nums in-place instead.
        """
        end_index = len(nums) - 1
        getIt = False
        while not getIt:
            if nums[end_index] <= nums[end_index - 1]:
                end_index -= 1
            else:
                for i in range(len(nums) - 1, end_index - 1, -1):
                    if nums[i] > nums[end_index - 1]:
                        temp = nums[i]
                        nums[i] = nums[end_index - 1]
                        nums[end_index - 1] = temp
                        # 将剩下的进行排序
                        seq = 0
                        for k in range(end_index, len(nums) - 1):
                            for j in range(end_index, len(nums) - 1 - seq):
                                if nums[j] > nums[j + 1]:
                                    temp = nums[j]
                                    nums[j] = nums[j + 1]
                                    nums[j + 1] = temp
                            seq += 1
                        getIt = True
                        break
            if end_index == 0:
                nums.reverse()
