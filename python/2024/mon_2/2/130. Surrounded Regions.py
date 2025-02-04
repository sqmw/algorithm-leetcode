import copy
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        T(n) = O(row_cou * column)
        借助了map减少时间复杂度，dict/map 的取值判定的时间复杂度为 O(1)
        """
        def recurse_get_path(index_i: int, index_j: int):
            """
            当前是 'O' 就加入，继续找，不是就返回
            :param index_i:
            :param index_j:
            :return:
            """
            nonlocal is_close
            if -1 < index_i < row_cou and -1 < index_j < column_cou:
                if board[index_i][index_j] == 'X' or (index_i * column_cou + index_j) in visited_dic:
                    return
                else:
                    if (index_i == row_cou - 1 or index_i == 0) or (index_j == column_cou - 1 or index_j == 0):
                        is_close = False
                    visited_dic[index_i * column_cou + index_j] = None
                    path.append((index_i, index_j))
                    # 需要四个方向
                    recurse_get_path(index_i - 1, index_j)
                    recurse_get_path(index_i, index_j + 1)
                    recurse_get_path(index_i + 1, index_j)
                    recurse_get_path(index_i, index_j - 1)

        row_cou: int = len(board)
        column_cou: int = len(board[0])
        path: List[tuple] = []
        visited_dic: dict[int, None] = {}
        is_close = True
        for i in range(row_cou):
            for j in range(column_cou):
                is_close = True
                if board[i][j] == 'O' and (i * column_cou + j) not in visited_dic:
                    # 找到所有相连的并且判断，是就全部转化
                    recurse_get_path(i, j)
                    if is_close is True:
                        for pos in path:
                            board[pos[0]][pos[1]] = 'X'
                    print(path)
                    path = []


if __name__ == '__main__':
    s = Solution()
    matrix = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
              ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
              ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
              ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
              ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
              ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
              ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
              ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
              ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
    for row in matrix:
        print(row)
    s.solve(matrix)
    print('-------------------------------------------------')
    for row in matrix:
        print(row)
