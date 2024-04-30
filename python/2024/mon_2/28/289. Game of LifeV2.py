from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        T(n): O(row * column)
        S(n): O(1){修改状态位可以表示当前的也可以表示之前的状态 二进制 ab表示状态变化是 a->b}
        # 下面的算法使用 2 表示 0 -> 1
        #              3 表示 1 -> 0
        """

        def init_is_one(_i: int, _j: int) -> bool:
            """
            仅仅是 1 的时候返回 1
            其他情况（无论是超出边界还是 0 ）返回False
            """
            if -1 < _i < len(board) and -1 < _j < len(board[0]):
                # board[_i][_j] >> 1 用来获取初始位
                if board[_i][_j] == 1 or board[_i][_j] == 2:
                    return True
                else:
                    return False

        # 判断周围的 8 个点
        def get_one_cou(_i, _j) -> int:
            cou: int = 0
            if init_is_one(_i - 1, _j - 1):
                cou += 1
            if init_is_one(_i - 1, _j):
                cou += 1
            if init_is_one(_i - 1, _j + 1):
                cou += 1
            if init_is_one(_i, _j + 1):
                cou += 1
            if init_is_one(_i + 1, _j + 1):
                cou += 1
            if init_is_one(_i + 1, _j):
                cou += 1
            if init_is_one(_i + 1, _j - 1):
                cou += 1
            if init_is_one(_i, _j - 1):
                cou += 1
            return cou

        for i in range(len(board)):
            for j in range(len(board[0])):
                one_cou: int = get_one_cou(i, j)
                if init_is_one(i, j) == 1:
                    if not (one_cou == 2 or one_cou == 3):
                        # 2 表示 1 -> 0
                        board[i][j] = 2
                # 0
                else:
                    if one_cou == 3:
                        # 3 表示 0 -> 1
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0


if __name__ == "__main__":
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board)
    print(board)
