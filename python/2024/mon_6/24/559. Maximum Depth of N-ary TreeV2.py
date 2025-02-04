# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        T(n): O(n)
        S(n): O(n)
        使用回溯法解决
        """
        if root is None:
            return 0
        path: List['Node'] = [root]
        des_len: int = 1

        def dfs(_root: 'Node'):
            nonlocal des_len
            if _root is None:
                return
            for child in _root.children:
                path.append(child)
                des_len = max(des_len, len(path))
                dfs(child)
                path.pop()

        dfs(root)
        return des_len
