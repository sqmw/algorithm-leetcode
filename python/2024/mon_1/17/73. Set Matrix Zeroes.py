from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row: set[int] = set()
        zero_column: set[int] = set()
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                zero_row.add(i)
                for j in [index for index, v in enumerate(matrix[i]) if v == 0]:
                    zero_column.add(j)
        for zero_row_index in zero_row:
            for i in range(len(matrix[zero_row_index])):
                matrix[zero_row_index][i] = 0

        for zero_column_index in zero_column:
            for i in range(len(matrix)):
                matrix[i][zero_column_index] = 0


if __name__ == '__main__':
    s = Solution()
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix)
    print(matrix)
