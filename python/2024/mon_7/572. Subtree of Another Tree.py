# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, Dict, List

from python.util.core.tree_util import *


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        T(n): O(nlog(n))
        S(n): O(n)
        每个 子树都建立一个先序和中序遍历的列表，如果两者相同，那么就是符合的
        :param root:
        :param subRoot:
        :return:
        """

        def dfs_seq(d_root: Optional[TreeNode]) -> tuple[List, List]:
            des_t: tuple[List, List] = ([], [])

            def _dfs(_root: Optional[TreeNode]):
                if _root is None:
                    return
                # 得到先序遍历的结果
                des_t[0].append(_root.val)
                _dfs(_root.left)
                # 得到中序遍历的结果
                des_t[1].append(_root.val)
                _dfs(_root.right)

            _dfs(d_root)
            return des_t

        sub_root_seq = dfs_seq(subRoot)
        have_same: bool = False

        def dfs(_root: Optional[TreeNode]):
            nonlocal have_same
            if _root is None or have_same is True:
                return
            if dfs_seq(_root) == sub_root_seq:
                have_same = True
                return
            dfs(_root.left)
            dfs(_root.right)

        dfs(root)

        return have_same


if __name__ == '__main__':
    s = Solution()
    print(s.isSubtree(list2tree_breadth_first_traverse([3, 4, 5, 1, 2]), list2tree_breadth_first_traverse([4, 1, 2])))
