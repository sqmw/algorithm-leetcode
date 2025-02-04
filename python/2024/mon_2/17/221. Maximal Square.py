from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        method1: 动态规划
        T(n): O(row * column)
        S(n): O(row * column)

        rec_f[i][j] 表示包括 matrix[i][j] 这个点的左上方的最大正方形
        method2: 直接右下方搜索，时间复杂度可能难以通过
        """
        row = len(matrix)
        column = len(matrix[0])

        rec_f = [[-1 for _ in range(column)] for _ in range(row)]

        # 表示正方形的最大边长
        a = 0
        # 需要先处理第一行、第一列
        for i in range(column):
            rec_f[0][i] = int(matrix[0][i])
            a = max(a, rec_f[0][i])
        for i in range(row):
            rec_f[i][0] = int(matrix[i][0])
            a = max(a, rec_f[i][0])

        for i in range(1, row):
            for j in range(1, column):
                if rec_f[i][j] == -1:
                    if matrix[i][j] == '1':
                        rec_f[i][j] = 1 + min(rec_f[i][j - 1], rec_f[i - 1][j], rec_f[i - 1][j - 1])
                        a = max(a, rec_f[i][j])
                    else:
                        rec_f[i][j] = 0

        return a ** 2


if __name__ == "__main__":
    s = Solution()
    matrix = [["1", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "0"],
              ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["0", "0", "1", "1", "1"]]
    print(s.maximalSquare(matrix))
