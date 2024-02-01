from typing import *
"""
再次熟悉二分法
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_i = len(matrix)
        len_j = len(matrix[0])

        def get_ij(index: int) -> tuple:
            return index // len_j, index % len_j

        left = 0
        right = len_i * len_j - 1
        while left <= right:
            mid = int((left + right) / 2)
            ij = get_ij(mid)
            if matrix[ij[0]][ij[1]] == target:
                return True
            elif target < matrix[ij[0]][ij[1]]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
