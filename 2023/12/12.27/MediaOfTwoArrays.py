from typing import List
'''
-- 使用的是普通方法，就是找到中间数字的位置
-- 还有一个方法是二分查找的方法，但是实现起来微调很复杂
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        arr = []
        media_index = int((len1 + len2 - 1) / 2)
        print(media_index)

        while len(arr) < len1 + len2:
            if i >= len1:
                while j < len2:
                    arr.append(nums2[j])
                    j += 1
                break
            if j >= len2:
                while i < len1:
                    arr.append(nums1[i])
                    i += 1
                break
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        print(arr)
        # 表示的是数据的长度是奇数
        if (len1 + len2) % 2 != 0:
            return arr[media_index]
        # 如果是偶数的话，取两个的平均值
        else:
            return (arr[media_index] + arr[media_index + 1]) / 2


print(Solution.findMedianSortedArrays(1, [1], [1,5]))
