from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        通过动态规划实现
        T(n): O(n)
        S(n): O(n)
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        else:
            rob_recur_f_start_zero = [0] * len(nums)
            rob_recur_f_start_zero[0] = nums[0]
            rob_recur_f_start_zero[1] = max(nums[0], nums[1])
            rob_recur_f_start_zero[2] = max(nums[1], nums[0] + nums[2])

            rob_recur_f_start_one = [0] * len(nums)
            rob_recur_f_start_one[1] = nums[1]
            rob_recur_f_start_one[2] = max(nums[1], nums[2])

            for i in range(3, len(nums)):
                rob_recur_f_start_zero[i] = max(rob_recur_f_start_zero[i - 2] + nums[i], rob_recur_f_start_zero[i - 1])
                rob_recur_f_start_one[i] = max(rob_recur_f_start_one[i - 2] + nums[i], rob_recur_f_start_one[i - 1])

            des_val = max(rob_recur_f_start_zero[len(nums) - 2], rob_recur_f_start_zero[len(nums) - 3],
                          rob_recur_f_start_one[len(nums) - 1], rob_recur_f_start_one[len(nums) - 2])

            return des_val


if __name__ == "__main__":
    s = Solution()
    print(s.rob([200, 3, 140, 20, 10]))
