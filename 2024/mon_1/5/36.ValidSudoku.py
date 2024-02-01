from typing import List


class Solution:
    digit_dic = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判定行
        for i in range(0, 9):
            my_dic = self.digit_dic.copy()
            for j in range(0, 9):
                if my_dic.get(board[i][j]) is not None:
                    my_dic[board[i][j]] += 1
                    if my_dic[board[i][j]] > 1:
                        return False
        # 列
        for i in range(0, 9):
            my_dic = self.digit_dic.copy()
            for j in range(0, 9):
                if my_dic.get(board[j][i]) is not None:
                    my_dic[board[j][i]] += 1
                    if my_dic[board[j][i]] > 1:
                        return False
        # 判断 3 * 3
        for i in range(0, 3):
            for j in range(0, 3):
                my_dic = self.digit_dic.copy()
                # 这上面的表示的是每一个大的
                for m in range(0, 3):
                    for n in range(0, 3):
                        r = 3 * i + m
                        c = 3 * j + n
                        if my_dic.get(board[r][c]) is not None:
                            my_dic[board[r][c]] += 1
                            if my_dic[board[r][c]] > 1:
                                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                              , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                              , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                              , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                              , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                              , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                              , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                              , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                              , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
