from typing import List, Set


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        使用回溯法，难度中等(题目标注的是 easy)
        T(n): O(n * m)
        S(n): O(n * m)
        """

        perimeter: int = 0
        edge_pos_set: Set[tuple] = set()
        # 得到边界点集
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i - 0.5, j - 0.5) not in edge_pos_set:
                        edge_pos_set.add((i - 0.5, j - 0.5))
                    if (i - 0.5, j + 0.5) not in edge_pos_set:
                        edge_pos_set.add((i - 0.5, j + 0.5))
                    if (i + 0.5, j + 0.5) not in edge_pos_set:
                        edge_pos_set.add((i + 0.5, j + 0.5))
                    if (i + 0.5, j - 0.5) not in edge_pos_set:
                        edge_pos_set.add((i + 0.5, j - 0.5))
        # 边界寻路
        # 使用回溯法(广度优先遍历)
        visited_set: Set[tuple] = set()
        start_pos = list(edge_pos_set)[0]

        def traceback(now_pos: tuple):
            nonlocal visited_set, edge_pos_set
            # 上右下左
            if now_pos == start_pos and len(visited_set) != 0:
                print(len(visited_set))
                return
            if now_pos not in edge_pos_set or now_pos in visited_set:
                return

            visited_set.add(now_pos)
            traceback((now_pos[0] - 1, now_pos[1]))
            traceback((now_pos[0], now_pos[1] + 1))
            traceback((now_pos[0] + 1, now_pos[1]))
            traceback((now_pos[0], now_pos[1] - 1))

        print(edge_pos_set)
        print(len(edge_pos_set))
        print(start_pos)
        return perimeter


if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter(grid=[[1, 1],
                                  [1, 1]]))
