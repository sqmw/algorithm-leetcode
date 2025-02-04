from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        起点权衡利弊、得心应手
        T(n): O(m + n)
        S(n): O(1)
        """
        row_cou = len(matrix)
        column_cou = len(matrix[0])
        i_start, j_start = row_cou - 1, 0
        while i_start > -1 and j_start < column_cou:
            if matrix[i_start][j_start] == target:
                return True
            elif target < matrix[i_start][j_start]:
                i_start -= 1
            else:
                j_start += 1
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 30
    print(s.searchMatrix(matrix, target))
