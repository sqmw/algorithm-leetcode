from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_set: 'Set' = set()
        for val in nums:
            if val in val_set:
                return True
            else:
                val_set.add(val)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
