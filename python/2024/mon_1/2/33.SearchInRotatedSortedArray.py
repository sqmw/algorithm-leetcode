from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 2:
            if target not in nums:
                return -1
            else:
                if nums[0] == target:
                    return 0
                else:
                    return 1
        # 先试用二分法找到划分的位置，再利用划分的位置进行两次的二分查找
        l_index = 0
        r_index = len(nums) - 1
        move_pos = 0
        if nums[l_index] > nums[r_index]:
            while True:
                if nums[l_index] > nums[r_index]:
                    m_index = int((l_index + r_index) / 2)
                    if nums[l_index] < nums[m_index]:
                        l_index = m_index
                    else:
                        r_index = m_index
                    if r_index - l_index == 1:
                        move_pos = len(nums) - r_index
                        break
        print(move_pos)
        max_index = len(nums) - 1 - move_pos
        min_index = (max_index + 1) % len(nums)
        print(min_index, max_index)
        if target < nums[min_index] or target > nums[max_index]:
            return -1
        else:
            if nums[min_index] <= target <= nums[len(nums) - 1]:
                return self.bisearch(min_index, len(nums) - 1, nums, target)
            else:
                return self.bisearch(0, max_index, nums, target)

    def bisearch(self, l_index, r_index, nums, target) -> int:
        while r_index - l_index > 1:
            if target == nums[l_index]:
                return l_index
            elif target == nums[r_index]:
                return r_index
            else:
                m_index = int((l_index + r_index) / 2)
                if target <= nums[m_index]:
                    r_index = m_index
                else:
                    l_index = m_index
        if target == nums[l_index]:
            return l_index
        elif target == nums[r_index]:
            return r_index
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([3, 5], 5))
