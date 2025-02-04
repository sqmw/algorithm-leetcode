# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        使用先序中序后序以及层次遍历都是可以的
        T(n): O(n)
        S(n): O(log(n))
        """

        def pre_traverse(_root: Optional[TreeNode]):
            nonlocal des_cou
            if _root is None:
                return

            if _root.left is not None and _root.left.left is None and _root.left.right is None:
                des_cou += _root.left.val
            pre_traverse(_root.left)
            pre_traverse(_root.right)

        des_cou = 0
        pre_traverse(root)
        return des_cou
