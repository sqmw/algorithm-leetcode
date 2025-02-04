import collections
from typing import List, Set, Dict


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        T(n): O(n**2) # 超时
        S(n): O(1)
        第 k 大的，等于第 (n + 1 - k 小)
        """
        nums_count_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        for item in nums:
            nums_count_dic[item] += 1
        if k < len(nums) // 2:
            for _ in range(k - 1):
                val_max = max(nums_count_dic.keys())
                if nums_count_dic[val_max] == 1:
                    nums_count_dic.pop(val_max)
                else:
                    nums_count_dic[val_max] -= 1
            return max(nums_count_dic)
        else:
            for _ in range(len(nums) - k):
                val_min = min(nums_count_dic.keys())
                if nums_count_dic[val_min] == 1:
                    nums_count_dic.pop(val_min)
                else:
                    nums_count_dic[val_min] -= 1
            return min(nums_count_dic)


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(s.findKthLargest(nums, k))
