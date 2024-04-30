from typing import List, Union

"""
这道题目十分不清晰，解答需要的相邻不是我们所认为的相邻
下面的解法是只要是超出的相邻也是相邻
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def can_try(_i, _j) -> bool:
            if (_i, _j) in path or _i < 0 or _i >= m or _j < 0 or _j >= n:
                return False
            return True

        def get_next_start_pos(_p_i, _p_j) -> Union[tuple | None]:
            """
            从左往右
            从上到下
            :param _p_i: 表示上一个起点 i
            :param _p_j: 表示上一个起点的 j
            :return: None->结束了，已经没有可以开始的点了
            """
            for _i in range(_p_i, m):
                if _i == _p_i:
                    for _j in range(_p_j + 1, n):
                        if board[_i][_j] == word[0]:
                            return _i, _j
                else:
                    for _j in range(0, n):
                        if board[_i][_j] == word[0]:
                            return _i, _j
            return None

        def traceback(pre_i: int, pre_j: int):
            """
            :param pre_i: 当前位置的 i
            :param pre_j: 当前位置的 j
            :return:
            """
            nonlocal exist
            nonlocal board
            nonlocal path_len_or_word_index
            if exist:
                return
            else:
                # print(path)
                # 表示四个方向
                if can_try(pre_i - 1, pre_j) and board[pre_i - 1][pre_j] == word[path_len_or_word_index]:
                    path.append((pre_i - 1, pre_j))
                    path_len_or_word_index += 1
                    if len(path) == len(word):
                        exist = True
                        return
                    traceback(pre_i - 1, pre_j)
                    path.pop()
                    path_len_or_word_index -= 1
                if can_try(pre_i, pre_j + 1) and board[pre_i][pre_j + 1] == word[path_len_or_word_index]:
                    path.append((pre_i, pre_j + 1))
                    path_len_or_word_index += 1
                    if len(path) == len(word):
                        exist = True
                        return
                    traceback(pre_i, pre_j + 1)
                    path.pop()
                    path_len_or_word_index -= 1
                if can_try(pre_i + 1, pre_j) and board[pre_i + 1][pre_j] == word[path_len_or_word_index]:
                    path.append((pre_i + 1, pre_j))
                    path_len_or_word_index += 1
                    if len(path) == len(word):
                        exist = True
                        return
                    traceback(pre_i + 1, pre_j)
                    path.pop()
                    path_len_or_word_index -= 1
                if can_try(pre_i, pre_j - 1) and board[pre_i][pre_j - 1] == word[path_len_or_word_index]:
                    path.append((pre_i, pre_j - 1))
                    path_len_or_word_index += 1
                    if len(path) == len(word):
                        exist = True
                        return
                    traceback(pre_i, pre_j - 1)
                    path.pop()
                    path_len_or_word_index -= 1

        exist = False
        path: List[tuple] = []
        path_len_or_word_index = 0
        # 找起点
        ij_pre = get_next_start_pos(0, -1)
        while ij_pre:
            path.append((ij_pre[0], ij_pre[1]))
            path_len_or_word_index += 1
            if len(path) == len(word):
                return True
            traceback(ij_pre[0], ij_pre[1])
            if len(path) > 0:
                path.pop()
                path_len_or_word_index -= 1
            ij_pre = get_next_start_pos(ij_pre[0], ij_pre[1])
        return exist


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"],
                   ["A", "A", "A", "A", "A", "A"]],
                  "AAAAAAAAAAAAAAB"))
