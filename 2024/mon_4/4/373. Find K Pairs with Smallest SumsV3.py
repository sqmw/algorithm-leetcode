import heapq
from typing import List, Set


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        1. 两个数组都是非递减序列，二元组里面第一个需要来自 nums1 第二个来自 nums2
        2. 每一个在 num1 里面的数字最多能和 nums2 里面的数字每个都匹配依次, nums2 也是
        3. 双指针

        method1:
        1. 采用归并思想(归并的过程中每次都需要给每个数字指定下一次判定，每次都需要加入一个新的数字，比较麻烦，目前还是没有采用)
        T(n): O(n)
        S(n): O(n)

        method2:
        使用堆
        T(n): O(k*log(n)) # 超时
        S(n): O(k)

        method3:
        1. 使用二分法实现


        下面的代码采用<堆> 和 set 来实现的
        """

        if not nums1 or not nums2:
            return []
        visited_pos: Set[tuple] = {(0, 0)}
        des_nums_list: List[List[int]] = []
        _heap = [(nums1[0] + nums2[0], 0, 0)]
        while len(des_nums_list) < k:
            _popped_sum, _popped_i, _popped_j = heapq.heappop(_heap)
            _sum01 = nums1[_popped_i] + nums2[_popped_j + 1] if _popped_j + 1 < len(nums2) else float('inf')
            _sum10 = nums1[_popped_i + 1] + nums2[_popped_j] if _popped_i + 1 < len(nums1) else float('inf')

            des_nums_list.append([nums1[_popped_i], nums2[_popped_j]])
            # 这里有点类似回溯
            if (_popped_i, _popped_j + 1) not in visited_pos:
                visited_pos.add((_popped_i, _popped_j + 1))
                heapq.heappush(_heap, (_sum01, _popped_i, _popped_j + 1))
            if (_popped_i + 1, _popped_j) not in visited_pos:
                visited_pos.add((_popped_i + 1, _popped_j))
                heapq.heappush(_heap, (_sum10, _popped_i + 1, _popped_j))

        return des_nums_list


if __name__ == "__main__":
    s = Solution()
    # @formatter:off
    assert s.kSmallestPairs(nums1=[1, 2, 4, 5, 6], nums2=[3, 5, 7, 9], k=20) == [[1, 3], [2, 3], [1, 5], [2, 5], [4, 3], [1, 7], [5, 3], [2, 7], [4, 5], [6, 3], [1, 9], [5, 5], [2, 9], [4, 7], [6, 5], [5, 7], [4, 9], [6, 7], [5, 9], [6, 9]]
    # @formatter:on
