from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            if _max < nums[i]:
                _max = nums[i]
        return _max


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
