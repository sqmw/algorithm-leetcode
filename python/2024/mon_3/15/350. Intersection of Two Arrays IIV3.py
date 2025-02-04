from typing import List


class Solution:
    def intersect(self, nums1, nums2):
        """
        method2: 使用排序，然后查找重复
        T(n): O(nlog(n) + mlog(m))
        S(n): O(des_arr_len)
        """
        nums1.sort()
        nums2.sort()

        des_arr: List[int] = []
        i = 0
        j = 0
        # 先让 nums2 去追 nums1，下标的变化过程中其实是两个互相追赶
        while i < len(nums1) and j < len(nums2):
            while j < len(nums2) and nums2[j] < nums1[i]:
                j += 1
            if j < len(nums2) and nums1[i] == nums2[j]:
                des_arr.append(nums1[i])
                j += 1
            i += 1

        return des_arr


if __name__ == "__main__":
    s = Solution()
    # 示例：
    nums1 = [1, 2]
    nums2 = [1, 1]
    print(s.intersect(nums1, nums2))  # 输出应为 [2, 2]
