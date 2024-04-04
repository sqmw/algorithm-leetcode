# Definition for a binary tree node.
import collections
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
        :param root:
        :return:
        T(n): O(n)
        S(n): O(log(n))
        """
        des_cou = 0

        _queue = collections.deque([root])
        while len(_queue) > 0:
            _now_len = len(_queue)
            for _ in range(_now_len):
                popped_node = _queue.popleft()
                if popped_node is not None:
                    _queue.append(popped_node.left)
                    _queue.append(popped_node.right)
                    if popped_node.left is not None and popped_node.left.left is None and popped_node.left.right is None:
                        des_cou += popped_node.left.val
        return des_cou
