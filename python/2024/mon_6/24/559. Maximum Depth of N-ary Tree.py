# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


import collections


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        T(n): O(n)
        S(n): O(n)
        :param root:
        :return:
        """
        if root is None:
            return 0
        _queue: collections.deque = collections.deque([root])
        des_len: int = 0
        while len(_queue) > 0:
            des_len += 1
            out_len = len(_queue)
            for _ in range(out_len):
                outed: 'Node' = _queue.popleft()
                for child in outed.children:
                    _queue.append(child)
        return des_len
