# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, Dict

from python.util.core.tree_util import *


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        :param root:
        :return:
        """
        des_sum: int = 0
        node_weight_dic: Dict[Optional[TreeNode]: int] = collections.defaultdict(lambda: 0)

        def dfs(_root: Optional[TreeNode]):
            nonlocal des_sum
            if _root is None:
                return
            dfs(_root.left)
            dfs(_root.right)
            # 出节点了
            node_weight_dic[_root] = node_weight_dic[_root.left] + node_weight_dic[_root.right] + _root.val
            des_sum += abs(node_weight_dic[_root.left] - node_weight_dic[_root.right])

        dfs(root)
        return des_sum


if __name__ == "__main__":
    null = None
    s = Solution()
    print(s.findTilt(list2tree_breadth_first_traverse([4, 2, 9, 3, 5, null, 7])))
