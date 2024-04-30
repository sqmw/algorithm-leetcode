from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_index = 0
        r_index = len(nums) - 1
        while r_index - l_index > 1:
            if nums[l_index] == target:
                return l_index
            elif nums[r_index] == target:
                return r_index
            m_index = int((l_index + r_index) / 2)
            if target < nums[m_index]:
                r_index = m_index
            else:
                l_index = m_index
        if nums[l_index] == target:
            return l_index
        elif nums[r_index] == target:
            return r_index
        if target < nums[l_index]:
            if l_index == 0:
                return 0
            return l_index - 1
        elif target > nums[r_index]:
            return r_index + 1
        else:
            return l_index + 1


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4, 5, 8], 9))
