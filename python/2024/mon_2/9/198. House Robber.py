from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划实现
        结果一定在末尾的两个里面，迭代使用的数组可以省掉，此时：
            T(n): O(n)
            S(n): O(1)
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[2] + nums[0])
        rec_f: List[int] = [nums[0], nums[1], nums[2] + nums[0]] + [0] * (len(nums) - 3)
        for i in range(2, len(nums)):
            rec_f[i] = nums[i] + max(rec_f[i - 2], rec_f[i - 3])
        return max(rec_f[len(nums) - 1], rec_f[len(nums) - 2])


if __name__ == "__main__":
    print(Solution().rob([1, 3, 1]))
