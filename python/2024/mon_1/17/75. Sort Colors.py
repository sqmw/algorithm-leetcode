from typing import List

"""
使用许选择排序
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_index = i
            for j in range(i, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            t = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = t


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    print(nums)
