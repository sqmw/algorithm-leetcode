import sys
from typing import List, Optional


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        1,2,3,4,5,6,7,8,9,10
        method1：# 逻辑有错误，应该将大于等于最小的长度的路径都存起来(作为候选值)
            1. 通过选中的节点，递归定义一个二叉树，选择出所有二叉树里面的最小的每个最长和
                - 也就是需要的返回值是所有最小的里面的最大的那个
            2. 可以进行简化，使用动态规划实现
        T(n): O(n**2)
        S(n): O(n)
        :param n:
        :return:
        """
        if n < 4:
            return n - 1

        def cal_sum_min(left_tuple: tuple, right_tuple: tuple, _root) -> (int, int):
            """
            这里的时间复杂度可以优化为 O(1)
            :param left_tuple: (start, node_cou)
            :param right_tuple:
            :param _root: _root_val
            :return: _sum, which_max(-1, 1)
            """
            _left_sum = 0
            _right_sum = 0
            # _left_sum = sum(偏移量) + base * cou
            _left_sum = sum(rec_f[left_tuple[1]]) + left_tuple[0] * len(rec_f[left_tuple[1]])
            _right_sum = sum(rec_f[right_tuple[1]]) + right_tuple[0] * len(rec_f[right_tuple[1]])
            if _left_sum > _right_sum:
                return _left_sum + _root, -1
            return _right_sum + _root, 1

        # rec_f[i] 表示的是长度 为 i 对应的 index 从 0 开始的计算得到的最小, rec_f 是一个二位矩阵
        rec_f: List[List[List[int]]] = [[] for _ in range(n + 1)]
        # 1,2,3,4,5,...,n
        # 下标分别是
        # 0,1 2 3,4,...,n-1
        rec_f[2] = [[0]]
        rec_f[3] = [[1]]
        # i 表示的是总的节点数量
        for i in range(4, n + 1):
            # j 表示把 j 当做最开始的父节点，此时我们就可以计算得到当前 j 最为父节点的最小的代价
            _min_parent = 1
            _sum_min = sys.maxsize
            _left_right = 0
            for j in range(1, i + 1):
                # 左边节点的数量: j - 1 左边开始 1
                # 右边节点的数量: i - j 右边开始 j + 1
                _sum_and_pos = cal_sum_min((1, j - 1), (j + 1, i - j), j)
                if _sum_min >= _sum_and_pos[0]:
                    _min_parent = j
                    _left_right = _sum_and_pos[1]
                    _sum_min = _sum_and_pos[0]
            # 根据 _min_parent 来构造 rec_f[i]
            _left_indexes = rec_f[_min_parent - 1].copy()
            # 因为使用的是 indexes 所以这里需要 - 1
            _left_indexes.append(_min_parent - 1)
            _right_indexes = rec_f[i - _min_parent].copy()
            for k in range(len(_right_indexes)):
                _right_indexes[k] += _min_parent
            # rec_f[i] 只能 等于 左边或者右边
            if _left_right == -1:
                rec_f[i] = _left_indexes
            else:
                rec_f[i] = [_min_parent - 1]
                rec_f[i].extend(_right_indexes)
        print(rec_f)
        return sum(rec_f[-1]) + len(rec_f[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.getMoneyAmount(16))
