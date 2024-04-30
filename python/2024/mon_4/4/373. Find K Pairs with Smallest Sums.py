import collections
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        两个数组都是非递减序列，二元组里面第一个需要来自 nums1 第二个来自 nums2

        method1:
        1. 采用归并思想
        T(n): O(n)
        S(n): O(n)
        method2:
        排序 / 使用堆
        T(n): O(nlog(n)) - O(n*m) # 超时
        S(n): O(n)

        使用 method1 需要考虑的边界比较麻烦，这里采用方法二实现
        """

        nums1_deque = collections.deque(nums1)
        nums2_deque = collections.deque(nums2)
        _heap = []
        des_temp = []
        while len(des_temp) < k:
            if len(nums2_deque) == 0 or len(nums1_deque) == 0:
                break
            first_min = min(nums1_deque[0], nums2_deque[0])
            if first_min == nums1_deque[0]:
                nums1_deque.popleft()
                for item in nums2_deque:
                    _heap.append((first_min + item, [first_min, item]))
            else:
                nums2_deque.popleft()
                for item in nums1_deque:
                    # des_temp.append([first_min, item])
                    _heap.append((first_min + item, [item, first_min]))
            heapq.heapify(_heap)
            des_temp.append(heapq.heappop(_heap)[1])
        while len(des_temp) < k:
            des_temp.append(heapq.heappop(_heap)[1])
        return des_temp


if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs(nums1=[1, 2, 3, 4, 5, 6], nums2=[3, 5, 7, 9], k=20))
