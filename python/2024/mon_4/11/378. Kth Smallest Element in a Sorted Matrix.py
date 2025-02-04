import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        # 实际上需要找的 index == k - 1
        method1:
            这里使用了归并的思想，借助 堆 来实现
        T(n): O(k*log(n))
        S(n): O(n)
        """
        rows_column_index_arr: List[int] = [0] * len(matrix)
        now_cou_index = 0
        _heap = []
        for i in range(len(matrix)):
            heapq.heappush(_heap, (matrix[i][rows_column_index_arr[i]], i))
        while True:
            for i in range(len(matrix)):
                val, row = heapq.heappop(_heap)
                rows_column_index_arr[row] += 1
                if rows_column_index_arr[row] < len(matrix[0]):
                    heapq.heappush(_heap, (matrix[row][rows_column_index_arr[row]], row))
                now_cou_index += 1
                if now_cou_index > k - 1:
                    return val


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix=[[1, 5, 9],
                                [10, 11, 13],
                                [12, 13, 15]], k=8))
