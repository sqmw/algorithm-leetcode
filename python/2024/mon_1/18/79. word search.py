from typing import List, Union

"""
这道题目十分不清晰，解答需要的相邻不是我们所认为的相邻
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def can_try(_i, _j) -> bool:
            if ((_i + m) % m, (_j + n) % n) in path:
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

        def get_next_may_suit_pos(_p_i, _p_j, _pre_pos=-1) -> Union[tuple | None]:
            """
            上:0 右:1 下:2 左:3
            :param _p_i:
            :param _p_j:
            :param _pre_pos: 用来限制走过的路,1 表示上一条是 1 即 0 和 1 都走过了
            :return:
            """
            if can_try(_p_i - 1, _p_j) and board[_p_i - 1][_p_j] == word[index_words] and 0 > _pre_pos:
                return (_p_i - 1 + m) % m, _p_j, 0
            elif can_try(_p_i, _p_j + 1) and board[_p_i][(_p_j + 1 + n) % n] == word[index_words] and 1 > _pre_pos:
                return _p_i, (_p_j + 1 + n) % n, 1
            elif can_try(_p_i + 1, _p_j) and board[(_p_i + 1 + m) % m][_p_j] == word[index_words] and 2 > _pre_pos:
                return (_p_i + 1 + m) % m, _p_j, 2
            elif can_try(_p_i, _p_j - 1) and board[_p_i][_p_j - 1] == word[index_words] and 3 > _pre_pos:
                return _p_i, (_p_j - 1 + n) % n, 3
            return None

        def traceback(pre_i: int, pre_j: int, pre_pos=-1):
            nonlocal exist
            nonlocal index_words
            nonlocal one_cant_reach
            nonlocal board
            print(path, exist)
            if exist or one_cant_reach:
                return
            else:
                # 移动原则：起点位置
                next_may_suit_pos = get_next_may_suit_pos(pre_i, pre_j, pre_pos)
                if next_may_suit_pos:
                    path.append((next_may_suit_pos[0], next_may_suit_pos[1]))
                    pos_of_path.append(next_may_suit_pos[2])
                    index_words += 1
                    if len(path) == len(word):
                        exist = True
                    else:
                        traceback(next_may_suit_pos[0], next_may_suit_pos[1])
                # 表示无路可走
                else:
                    # 表示这条路走不通
                    ij = path.pop()
                    pre_pos = pos_of_path.pop()
                    index_words -= 1

                    if len(path) == 0:
                        one_cant_reach = True
                    else:
                        # 退一步，走上一步没走过的
                        traceback(path[len(path) - 1][0], path[len(path) - 1][1], pre_pos)

        index_words = None
        exist = False
        one_cant_reach = False
        path: List[tuple] = []
        pos_of_path: List[int] = []
        # 找起点
        ij_pre = get_next_start_pos(0, -1)

        while ij_pre:
            # print(ij_pre)
            index_words = 1
            one_cant_reach = False
            path.append((ij_pre[0], ij_pre[1]))
            pos_of_path.append(-1)
            if len(path) == len(word):
                return True
            traceback(ij_pre[0], ij_pre[1])
            if len(path) > 0:
                path.pop()
                pos_of_path.pop()
            ij_pre = get_next_start_pos(ij_pre[0], ij_pre[1])

        return exist


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["a","a","b","a","a","b"],
                   ["a","a","b","b","b","a"],
                   ["a","a","a","a","b","a"],
                   ["b","a","b","b","a","b"],
                   ["a","b","b","a","b","a"],
                   ["b","a","a","a","a","b"]], "bbbaabbbbbab"))
