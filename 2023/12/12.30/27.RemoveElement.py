from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_right = -1
        index_select = 0
        while index_select < len(nums):
            if nums[index_select] != val:
                index_right += 1
                nums[index_right] = nums[index_select]
            index_select += 1
        return index_right + 1


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(s.removeElement(a, 2))
    print(a)
