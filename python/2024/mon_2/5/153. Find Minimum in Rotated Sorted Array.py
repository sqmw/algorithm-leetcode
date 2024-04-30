import sys
from typing import List

"""
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
 0,1,2,3,4,5,6
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        T(n): O(log(n))
        S(n): O(1)
        :param nums:
        :return:
        """
        left = 0
        right = len(nums) - 1
        des_min = sys.maxsize
        while left <= right:
            mid = int((right + left) / 2)
            des_min = min(des_min, nums[mid], nums[left], nums[right])
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return des_min


if __name__ == '__main__':
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
