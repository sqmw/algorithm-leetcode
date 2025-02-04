from typing import List

"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output:       [5,6,7,1,2,3,4]
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T(n): O(k * n)
        S(n): O(1)
        """
        # r 表示末尾移到开始
        right = k % len(nums)
        # 开始移到末尾
        left = len(nums) - right
        if right < left:
            for i in range(right):
                nums.insert(0, nums.pop())
        else:
            for i in range(left):
                nums.append(nums[0])
                del nums[0]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    Solution().rotate(nums, k)
    print(nums)
