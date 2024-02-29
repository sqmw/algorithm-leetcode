from typing import List

"""
target = 7
nums = [2,3,1,2,4,3]
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        _min_len = len(nums)
        left = 0
        right = 1
        while right <= len(nums):
            if sum(nums[left: right]) < target:
                right += 1
            else:
                _min_len = min(_min_len, right - left)
                left += 1
        return _min_len


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    s = Solution()
    print(s.minSubArrayLen(nums=nums, target=target))
