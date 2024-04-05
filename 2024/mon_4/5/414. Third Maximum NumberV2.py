from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        T(n): O(n)
        S(n): O(n)
        """
        nums: List[int] = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        # 这里选择使用选择排序 # 每次都选择一个最大的数字
        for i in range(3):
            num_max_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[num_max_index]:
                    num_max_index = j
            nums[i], nums[num_max_index] = nums[num_max_index], nums[i]

        return nums[2]


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([3, 1, 2, 2]))
