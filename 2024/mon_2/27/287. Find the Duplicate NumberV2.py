from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        实现思路：由题目知道，数组长度为 n + 1 包含了 [1,n]的所有数字，找出其中唯一的出现两次的那个，那么按照这个条件复位即可
        """
        # num[index] == index + 1
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] != nums[i]:
                    a = i
                    b = nums[i] - 1
                    nums[a], nums[b] = nums[b], nums[a]
                else:
                    return nums[i]


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))
