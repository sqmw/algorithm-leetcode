# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        method1： 反向拷贝
        T(n): O(n)
        S(n): O(n)
        method2： 方向逆转
        T(n): O(n)
        S(n): O(h)[实际上是递归的深度(O(h))]
        """
        if root is None:
            return None
        inverted_tree: Optional[TreeNode] = TreeNode()

        def preorder_traverse(_root: Optional[TreeNode], _invert_root: Optional[TreeNode]):
            if _root is not None:
                _invert_root.val = _root.val
                if _root.left is not None:
                    _invert_root.right = TreeNode()
                    preorder_traverse(_root.left, _invert_root.right)
                if _root.right is not None:
                    _invert_root.left = TreeNode()
                    preorder_traverse(_root.right, _invert_root.left)

        preorder_traverse(root, inverted_tree)
        return inverted_tree


if __name__ == "__main__":
    s = Solution()
    print(tree_util.tree2list_pre_traverse(s.invertTree(tree_util.list2tree_breadth_first_traverse([1, 2, 3]))))
