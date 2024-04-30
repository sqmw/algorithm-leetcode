from typing import List


class Solution:
    def getPos(self, nums: List[int], target: int) -> int:
        l_index = 0
        r_index = len(nums) - 1
        while r_index - l_index > 1:
            if target < nums[l_index] or target > nums[r_index]:
                return -1
            if nums[l_index] == target:
                return l_index
            if nums[r_index] == target:
                return r_index
            m_index = int((l_index + r_index) / 2)
            if target < nums[m_index]:
                r_index = m_index
            else:
                l_index = m_index
        if nums[l_index] == target:
            return l_index
        if nums[r_index] == target:
            return r_index
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        m = self.getPos(nums, target)
        print(m)
        if m == -1:
            return [-1, -1]
        else:
            left_index = m
            right_index = m
            # 这里可以进行优化
            for i in range(m, -1, -1):
                if nums[i] == nums[m]:
                    left_index = i
            for i in range(m, len(nums)):
                if nums[i] == nums[m]:
                    right_index = i
            return [left_index, right_index]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([2, 2], 2))
