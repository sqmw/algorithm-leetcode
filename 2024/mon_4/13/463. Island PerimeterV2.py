from typing import List, Set


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        使用回溯法，难度中等(题目标注的是 easy)
        T(n): O(n * m)
        S(n): O(n * m)
        下面的方法最终没有使用回溯法，但是
        1. 下面的方法对边进行了抽象分离
        2. 是否不抽象出 edge，直接更具 1/0 来进行判断呢？显然是可以的
        """

        def is_edge_pos(_pos_i, _pos_j) -> bool:
            if (0.5 <= _pos_i <= len(grid) - 1.5 and 0.5 <= _pos_j <= len(grid[0]) - 1.5) and \
                    grid[int(_pos_i - 0.5)][int(_pos_j - 0.5)] == 1 and \
                    grid[int(_pos_i - 0.5)][int(_pos_j + 0.5)] == 1 and \
                    grid[int(_pos_i + 0.5)][int(_pos_j + 0.5)] == 1 and \
                    grid[int(_pos_i + 0.5)][int(_pos_j - 0.5)] == 1:
                return False
            return True

        # 仅仅存储 edge， 内部的一律不存
        edge_pos_set: Set[tuple] = set()
        # 得到边界点集
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i - 0.5, j - 0.5) not in edge_pos_set and is_edge_pos(i - 0.5, j - 0.5):
                        edge_pos_set.add((i - 0.5, j - 0.5))
                    if (i - 0.5, j + 0.5) not in edge_pos_set and is_edge_pos(i - 0.5, j + 0.5):
                        edge_pos_set.add((i - 0.5, j + 0.5))
                    if (i + 0.5, j + 0.5) not in edge_pos_set and is_edge_pos(i + 0.5, j + 0.5):
                        edge_pos_set.add((i + 0.5, j + 0.5))
                    if (i + 0.5, j - 0.5) not in edge_pos_set and is_edge_pos(i + 0.5, j - 0.5):
                        edge_pos_set.add((i + 0.5, j - 0.5))
        return len(edge_pos_set)


if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter(grid=[[1, 1],
                                  [1, 1]]))
