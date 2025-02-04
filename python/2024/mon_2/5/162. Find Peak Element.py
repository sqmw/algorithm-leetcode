from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 2] < nums[len(nums) - 1]:
            return len(nums) - 1
        left = 1
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1] > nums[mid + 2]:
                return mid + 1
            # 表示往左走(贪心思想)
            if abs(nums[mid] - nums[left]) < mid - left or nums[left] >= nums[mid] or (nums[mid - 1] > nums[mid]):
                right = mid - 1
            else:
                left = mid + 1


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 5, 4, 3, 2, 1]))
