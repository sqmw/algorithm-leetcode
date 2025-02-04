from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        len_x = len(obstacleGrid)
        len_y = len(obstacleGrid[0])
        f = [[1 for _ in range(len_y)] for _ in range(len_x)]
        for i in range(len_x):
            for j in range(len_y):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                    continue
                if not (i == 0 or j == 0):
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
                elif i == 0:
                    f[i][j] = f[i][j - 1]
                else:  # 表示 j == 0
                    f[i][j] = f[i - 1][j]
        return f[len_x - 1][len_y - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
