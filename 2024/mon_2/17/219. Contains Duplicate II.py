import collections
from typing import List, Dict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        T(n): O(n)
        S(n): O(n)
        """
        # 用来记录上一次出现的下标
        num_dic: Dict[int, int] = collections.defaultdict(lambda: -1)
        for i in range(len(nums)):
            if i - num_dic[nums[i]] <= i and i - num_dic[nums[i]] < i <= k:
                return True
            num_dic[nums[i]] = i
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(s.containsNearbyDuplicate(nums, k))
