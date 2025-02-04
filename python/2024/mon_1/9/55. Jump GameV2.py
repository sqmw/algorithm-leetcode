from typing import List

"""
贪心算法实现
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums)):
            max_index = max(i + nums[i], max_index)
            if max_index >= len(nums) - 1:
                return True
            if i == max_index and nums[max_index] == 0:
                return False


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([3, 2, 1, 0, 1]))
