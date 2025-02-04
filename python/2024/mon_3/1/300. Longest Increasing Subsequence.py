from typing import List

"""
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence
        method1: 回溯法
            估计要超时，因为时间复杂度大于 O(n**2)
        method2： 动态规划
            T(n): O(n**2)
            S(n): O(n)
        """
        rec_f: List[int] = [1] * len(nums)
        # 遍历得到每一个 rec_f[i] 的最大值
        for i in range(len(nums)):
            each_max: int = 0
            # 遍历前面的所有值
            for j in range(i):
                if nums[j] < nums[i]:
                    each_max = max(each_max, rec_f[j])
            rec_f[i] += each_max
        # 这里产生了 O(n)的时间复杂度，可以在上面迭代的过程中就得到这个结果，但是代码清晰度会相应降低
        return max(rec_f)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
