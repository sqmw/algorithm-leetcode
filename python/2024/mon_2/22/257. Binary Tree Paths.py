#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        通过深度优先便利实现
        T(n): O(n)
        S(n): O(n)
        """
        des_list: List[str] = []
        path: List[int] = []

        def preorder_traverse(_root: Optional[TreeNode]):
            nonlocal path, des_list
            if _root is None:
                return
            if _root.left is None and _root.right is None:
                des_list.append('->'.join(map(str, path)))
            if _root.left is not None:
                path.append(_root.left.val)
                preorder_traverse(_root.left)
                path.pop()

            if _root.right is not None:
                path.append(_root.right.val)
                preorder_traverse(_root.right)
                path.pop()

        if root is not None:
            path.append(root.val)
            preorder_traverse(root)
            path.pop()

        return des_list


if __name__ == "__main__":
    s = Solution()
    null = None
    root = [1, 2, 3, null, 5]
    tree = tree_util.list2tree_breadth_first_traverse(root)
    print(s.binaryTreePaths(tree))
