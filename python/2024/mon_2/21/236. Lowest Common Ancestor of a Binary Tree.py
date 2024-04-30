#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Optional, List, Set

from python.util.core.tree_util import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_traverse(_root: Optional[TreeNode]):
            nonlocal path
            nonlocal p_path, q_path
            if _root == p:
                p_path = path[:]
            elif _root == q:
                q_path = path[:]
            if p_path is not None and q_path is not None:
                return
            if _root.left is not None:
                path.append(_root.left)
                recurse_traverse(_root.left)
                path.pop()
            if _root.right is not None:
                path.append(_root.right)
                recurse_traverse(_root.right)
                path.pop()

        path: List[TreeNode] = []
        p_path: Optional[List[TreeNode]] = None
        q_path: Optional[List[TreeNode]] = None

        if root is not None:
            path.append(root)
            recurse_traverse(root)
            path.pop()

        p_path_index_dic: Set[TreeNode] = set(p_path)
        for i in range(len(q_path) - 1, -1, -1):
            if q_path[i] in p_path_index_dic:
                return q_path[i]
