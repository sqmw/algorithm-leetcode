from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        二维空间的二分...没完全实现，
        通过递归更容易...代码似乎很复杂...性能还不讨好
        """
        row = len(matrix)
        column = len(matrix[0])
        i_start = 0
        j_start = 0

        i_end = row - 1
        j_end = column - 1

        i_mid = (i_start + i_end) // 2
        j_mid = (j_start + j_end) // 2

        # 向右上
        i = 1
        mid_max = matrix[0][0]
        mid_min = matrix[i_end][j_end]
        while True:
            if i_mid - i < 0 or j_mid + i > column - 1:
                break

            mid_min = min(mid_min, matrix[i_mid - i][j_mid + i])
            mid_max = max(mid_max, matrix[i_mid - i][j_mid + i])
            if matrix[i_mid - i][j_mid + i] == target:
                return True
            i += 1
        # 向左下
        i = 1
        mid_max = matrix[0][0]
        mid_min = matrix[i_end][j_end]
        while True:
            if i_mid + i > row - 1 or j_mid - i < 0:
                break
            mid_min = min(mid_min, matrix[i_mid + i][j_mid - i])
            mid_max = max(mid_max, matrix[i_mid + i][j_mid - i])
            if matrix[i_mid + i][j_mid - i] == target:
                return True
            i += 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[]], 1))
