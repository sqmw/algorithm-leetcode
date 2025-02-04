from typing import List, Set, Optional


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 上右下左
        # 任何一个范围，要么是要么不是
        """
        S(n): O(n)
        T(n): O(n)
        通过递归实现
        """

        def recurse2get_island(now_pos: tuple):
            if (now_pos[0] < 0 or now_pos[0] >= len(grid)) or (
                    now_pos[1] < 0 or now_pos[1] >= len(grid[0])) or now_pos in visited_pos_set:
                return
            if grid[now_pos[0]][now_pos[1]] == '1':
                visited_pos_set.add(now_pos)
                recurse2get_island((now_pos[0] - 1, now_pos[1]))
                recurse2get_island((now_pos[0], now_pos[1] + 1))
                recurse2get_island((now_pos[0] + 1, now_pos[1]))
                recurse2get_island((now_pos[0], now_pos[1] - 1))

        land_cou: int = 0
        visited_pos_set: Set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited_pos_set or grid[i][j] == '0':
                    continue
                else:
                    recurse2get_island((i, j))
                    land_cou += 1
        return land_cou


if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(s.numIslands(grid))
