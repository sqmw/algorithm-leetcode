from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        题目意思有问题，题目没有限制数字的范围值 [1, n]，下面的代码是一般解
        method1: 使用 hash
            T(n): O(n)
            S(n): O(n)
        method2: 直接对号入座
            indexes: 0 1 2 3 4
            nums   : 1 2 3 4 5
            T(n): O(n)
            S(n): O(1)
        :param nums:
        :return:
        """
        des_nums: List[int] = []
        # 调整源 nums 的位置
        for i in range(0, len(nums)):
            # 表示位置不对，进行调整
            if 1 <= nums[i] <= len(nums) and nums[i] != i + 1:
                while 1 <= nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                des_nums.append(i + 1)
        return des_nums


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
