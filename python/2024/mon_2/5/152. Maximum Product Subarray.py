from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        1. 使用 f_max[i] 表示 index == i 对应的最大值, f_min[i] 表示最小值
        :param nums:
        :return:
        优化：
            - 可以对代码进行空间的优化，使用 O(1) 的额外空间
        """
        f_max = [nums[0]] * len(nums)
        # 因为有负数，所以需要 des_min
        f_min = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            f_max[i] = max(nums[i], nums[i] * nums[i - 1], nums[i] * f_max[i - 1], nums[i] * f_min[i - 1])
            f_min[i] = min(nums[i], nums[i] * nums[i - 1], nums[i] * f_max[i - 1], nums[i] * f_min[i - 1])
        return max(f_max)


if __name__ == '__main__':
    print(Solution().maxProduct([-2, 0, -1]))
