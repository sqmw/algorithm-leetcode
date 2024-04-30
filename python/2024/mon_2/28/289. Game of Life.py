from typing import List, Set


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        T(n): O(row * column)
        S1(n): O(cou_one)
        S2(n): O(column){此时需要数组来保存参照位 S == 3 * column}
        S3(n): O(1){修改状态位可以表示当前的也可以表示之前的状态 二进制 ab表示状态变化是 a->b}
        """

        def get_one_cou(_i, _j) -> int:
            cou: int = 0
            if (_i - 1, _j - 1) in one_val_pos_set:
                cou += 1
            if (_i - 1, _j) in one_val_pos_set:
                cou += 1
            if (_i - 1, _j + 1) in one_val_pos_set:
                cou += 1
            if (_i, _j + 1) in one_val_pos_set:
                cou += 1
            if (_i + 1, _j + 1) in one_val_pos_set:
                cou += 1
            if (_i + 1, _j) in one_val_pos_set:
                cou += 1
            if (_i + 1, _j - 1) in one_val_pos_set:
                cou += 1
            if (_i, _j - 1) in one_val_pos_set:
                cou += 1
            return cou

        one_val_pos_set: Set[tuple] = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    one_val_pos_set.add((i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                one_cou: int = get_one_cou(i, j)
                if board[i][j] == 1:
                    if not (one_cou == 2 or one_cou == 3):
                        board[i][j] = 0
                # 0
                else:
                    if one_cou == 3:
                        board[i][j] = 1


if __name__ == "__main__":
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    s.gameOfLife(board)
    print(board)
