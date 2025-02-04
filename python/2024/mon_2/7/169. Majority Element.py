import collections
from typing import List, Dict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times_max_num: int = nums[0]
        num_cou_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        for item in nums:
            num_cou_dic[item] += 1
            if num_cou_dic[times_max_num] < num_cou_dic[item]:
                times_max_num = item
        return times_max_num


if __name__ == "__main__":
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
