import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # i' == n - 1 - j     j' = i
        """
        Do not return anything, modify matrix in-place instead.
        """
        old = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = old[n - 1 - j][i]


if __name__ == '__main__':
    s = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(s.rotate(matrix))
    print(matrix)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
