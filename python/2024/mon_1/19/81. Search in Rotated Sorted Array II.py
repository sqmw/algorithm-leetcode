from typing import List

"""
solution1: 直接顺序查找
solution2: 两次二分
 - 二分法的性能更好一些
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pre_stop_index = -1
        if len(nums) == 0:
            return False
        if nums[0] == target:
            return True
        for i in range(1, len(nums)):
            if nums[i] == target:
                return True
            if nums[i - 1] > nums[i]:
                pre_stop_index = i - 1
                break
        left = 0
        right = pre_stop_index
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        left = pre_stop_index + 1
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.search([5, 1, 3], 3))
