# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        通过遍历每一个节点得到数量
        T(n): O(n)
        S(n): O(h)
        """

        def preorder_traverse(_root: Optional[TreeNode]) -> None:
            nonlocal count
            if _root is not None:
                count += 1
                preorder_traverse(_root.left)
                preorder_traverse(_root.right)

        count = 0
        preorder_traverse(root)
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countNodes(tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4, 5, 6])))
