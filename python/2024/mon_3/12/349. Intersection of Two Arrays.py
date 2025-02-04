from typing import List, Set


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        method: 使用集合 hash 实现
            一般而言对于时间复杂度而言，只要是O(n)并且没有类似的二分法的解法，那么O(n)就是该算法的最有时间复杂度
        T(n): O(m + n)
        S(n): O(m + n)
        """
        nums1_set: Set = set(nums1)
        nums2_set: Set = set(nums2)

        des_list: List[int] = []
        for item in nums1_set:
            if item in nums2_set:
                des_list.append(item)

        return des_list


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))
