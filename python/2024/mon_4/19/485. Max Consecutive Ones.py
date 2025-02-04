from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        """
        i = 0
        _des_max_len: int = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i
                while j < len(nums) and nums[j] == 1:
                    j += 1
                _des_max_len = max(_des_max_len, j - i)
                i = j
            else:
                i += 1

        return _des_max_len


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
