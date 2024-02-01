from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_x = len(grid)
        len_y = len(grid[0])
        f = [[0 for _ in range(len_y)] for _ in range(len_x)]
        for i in range(len_x):
            for j in range(len_y):
                if not (i == 0 or j == 0):
                    f[i][j] = min(f[i - 1][j] + grid[i][j], f[i][j - 1] + grid[i][j])
                elif i == 0:
                    f[i][j] = f[i][j - 1] + grid[i][j]
                elif j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[0][0] = grid[0][0]

        return f[len_x - 1][len_y - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
