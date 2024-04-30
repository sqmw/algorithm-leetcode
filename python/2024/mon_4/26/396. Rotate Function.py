from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        F(k) = 0 * arrK[0] + 1 * arrK[1] + ... + (n - 1) * arrK[n - 1]
        使用动态规划进行求解(从动态规划的本质问题出发)
            1. 可以发现每两个相邻的 f(k) 之间的差是有数学表达式的
        T(n): O(n)
        S(n): O(1)
        """
        _init_sum = sum(nums)
        _last_f_sum: int = 0

        for i in range(len(nums)):
            _last_f_sum += i * nums[i]
        _max_f_sum: int = _last_f_sum
        _negative_last_index = len(nums) - 1
        for i in range(len(nums) - 1):
            _last_f_sum = _last_f_sum + (-(len(nums)) * nums[_negative_last_index] + _init_sum)
            _negative_last_index -= 1
            _max_f_sum = max(_max_f_sum, _last_f_sum)
        return _max_f_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxRotateFunction([4, 3, 2, 6]))
