import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        1. 两个数组都是非递减序列，二元组里面第一个需要来自 nums1 第二个来自 nums2
        2. 每一个在 num1 里面的数字最多能和 nums2 里面的数字每个都匹配依次, nums2 也是

        method1:
        1. 采用归并思想
        T(n): O(n)
        S(n): O(n)
        method2:
        排序 / 使用堆
        T(n): O(nlog(n)) - O(n*m) # 超时
        S(n): O(n)

        极致 / 追求
        本来想着偷点懒，使用第二个方法实现，但是时间复杂度还是过不了，只能使用方法 1 了
        """

        if not nums1 or not nums2:
            return []

        result = []
        heap = [(nums1[0] + nums2[0], 0, 0)]  # (sum, index of nums1, index of nums2)
        visited = {(0, 0)}  # Set to keep track of visited indices

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # Push the next possible pairs into the heap
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs(nums1=[1, 2, 4, 5, 6], nums2=[3, 5, 7, 9], k=20))
    print(
        [[1, 3], [2, 3], [1, 5], [2, 5], [4, 3], [1, 7], [5, 3], [2, 7], [4, 5], [6, 3], [1, 9], [5, 5], [2, 9], [4, 7],
         [6, 5], [5, 7], [4, 9], [6, 7], [5, 9], [6, 9]])
