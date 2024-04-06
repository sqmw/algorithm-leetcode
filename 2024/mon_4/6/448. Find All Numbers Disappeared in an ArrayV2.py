from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
