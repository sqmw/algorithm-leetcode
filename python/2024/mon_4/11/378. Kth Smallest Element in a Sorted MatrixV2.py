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
        n = len(matrix)
        rows_column_index_arr = [0] * n
        heap = []

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i))

        for _ in range(k - 1):
            val, row = heapq.heappop(heap)
            if rows_column_index_arr[row] < n - 1:
                rows_column_index_arr[row] += 1
                col = rows_column_index_arr[row]
                heapq.heappush(heap, (matrix[row][col], row))

        return heapq.heappop(heap)[0]


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix=[[1, 5, 9],
                                [10, 11, 13],
                                [12, 13, 15]], k=8))
