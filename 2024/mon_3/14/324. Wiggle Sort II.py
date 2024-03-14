from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < nums[5] > nums[6]
        method1:
            将原来的数组进行排序
            按照题目要求的序列，把偶数为设置为从大到小降序排列
            奇数位，同样按照从大到小一次排列
            T(n): O(nlog(n))
            S(n): O(n)
            ?是否可以参照快排的思想，每次确定一个位置呢?
        """
        nums.sort(reverse=True)
        new_nums = nums[:]
        for i in range(1, len(nums), 2):
            nums[i] = new_nums[(i - 1) // 2]
        start = len(nums) // 2
        for i in range(0, len(nums), 2):
            nums[i] = new_nums[start]
            start += 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(nums)
    print(nums)
