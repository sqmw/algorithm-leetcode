import collections
from typing import List, Dict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        method2：摩尔投票，可以证明最多只能有2个候选人
        T(n): O(n)
        S(n): O(1)
        """
        des_num_list: List[int] = []
        candidate1 = nums[0]
        cou1 = 1
        candidate2 = None
        cou2 = 0
        for i in range(1, len(nums)):
            if nums[i] == candidate1:
                cou1 += 1
            elif nums[i] == candidate2:
                cou2 += 1
            else:
                if cou1 == 0:
                    candidate1 = nums[i]
                    cou1 = 1
                elif cou2 == 0:
                    candidate2 = nums[i]
                    cou2 = 1
                else:
                    cou1 -= 1
                    cou2 -= 1
        candidate_dic: Dict[int, int] = dict()
        if cou1 > 0:
            candidate_dic[candidate1] = 0
        if cou2 > 0:
            candidate_dic[candidate2] = 0
        for num in nums:
            if num in candidate_dic:
                candidate_dic[num] += 1
        for candidate in candidate_dic.keys():
            if candidate_dic[candidate] > len(nums) // 3:
                des_num_list.append(candidate)
        return des_num_list


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1, 1, 2, 3,4]))
