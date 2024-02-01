# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
这道题花费的时间太长了，目前不想做
"""
import copy
from typing import List, Optional, Union
from util.core.tree_util import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        des_tree_arr: List[Optional[TreeNode]] = []
        # 取出队头的节点，进行添加
        path: List[Union[int | None]] = []
        now_tree = Optional[TreeNode] = TreeNode()

        # 给 root 添加节点
        f: List[Optional[List[Optional[TreeNode]]]] = []
        f[0] = None
        f[1] = [TreeNode(1)]
        f[2] = [TreeNode(1)]
        return des_tree_arr


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
