import collections
from typing import List, Dict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        method1：使用dict实现
        T(n): O(n)
        S(n): O(n)
        """
        des_num_list: List[int] = []
        num_cou_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        for num in nums:
            num_cou_dic[num] += 1
        for k in num_cou_dic.keys():
            if num_cou_dic[k] > len(nums) // 3:
                des_num_list.append(k)
        return des_num_list


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2, 3]))
