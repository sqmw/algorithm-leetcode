# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        题目给了这个是一个 BST
        可以通过递归查找实现,本身就是一个中序遍历
        T(n): O(n)
        S(n): O(log(n))
        """
        _min_diff: int = sys.maxsize
        _last_val = sys.maxsize

        def recurse2get_min_sum_diff(_root: Optional[TreeNode]):
            nonlocal _min_diff, _last_val
            if _root is None:
                return
            recurse2get_min_sum_diff(_root.left)
            _min_diff = min(_min_diff, abs(_last_val - _root.val))
            _last_val = _root.val
            recurse2get_min_sum_diff(_root.right)

        recurse2get_min_sum_diff(root)
        return _min_diff


if __name__ == "__main__":
    s = Solution()
    print(s.getMinimumDifference(tree_util.list2tree_breadth_first_traverse([4, 2, 6, 1, 3])))
