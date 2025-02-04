from typing import List

"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output:       [5,6,7,1,2,3,4]
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(start, end):
            while start < end:
                t = nums[start]
                nums[start] = nums[end]
                nums[end] = t
                start += 1
                end -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
