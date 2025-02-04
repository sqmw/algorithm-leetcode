import collections
from typing import List, Set, Dict


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        T(n): O(val_max - val_min)
        S(n): O(n)
        还可以使用堆排序或者快排实现
        """
        val_cou_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        for item in nums:
            val_cou_dic[item] += 1
        large_th = 0
        for i in range(max(nums), min(nums) - 1, -1):
            large_th += val_cou_dic[i]
            if large_th >= k:
                return i


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(s.findKthLargest(nums, k))
