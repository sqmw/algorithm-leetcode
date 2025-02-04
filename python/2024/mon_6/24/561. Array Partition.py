from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        des_sum: int = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            des_sum += nums[i]
        return des_sum
