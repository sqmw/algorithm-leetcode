import collections
from typing import List, Dict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        method1: 使用字典 hash<val,val_cou>
        T(n): O(len1 + len2)
        S(n): O(distinct_len1 + distinct_len2)
        """
        des_arr: List[int] = []
        nums1_dic: Dict[int, int] = collections.defaultdict(lambda: 0)
        nums2_dic: Dict[int, int] = collections.defaultdict(lambda: 0)

        for num in nums1:
            nums1_dic[num] += 1

        for num in nums2:
            nums2_dic[num] += 1

        # 在这里我们需要保证 len(nums1_dic) > len(nums2_dic)
        if len(nums1_dic) < len(nums2_dic):
            nums1_dic, nums2_dic = nums2_dic, nums1_dic
        for k in nums2_dic:
            if k in nums1_dic:
                des_arr.extend([k for _ in range(min(nums1_dic[k], nums2_dic[k]))])
        return des_arr


if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    s = Solution()
    print(s.intersect(nums1, nums2))
