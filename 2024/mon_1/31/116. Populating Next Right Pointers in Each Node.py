# Definition for a Node.
from typing import Optional, List

from util.core import tree_util


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return root
        _queue: List[Node] = [root]
        while len(_queue) > 0:
            level_len = len(_queue)

            for i in range(level_len):
                if i < level_len - 1:
                    _queue[0].next = _queue[1]
                _node: Node = _queue[0]
                del _queue[0]
                if _node is not None:
                    # 添加的过程保证每个节点都不是 None
                    if _node.left is not None:
                        _queue.append(_node.left)
                    if _node.right is not None:
                        _queue.append(_node.right)

        return root


if __name__ == "__main__":
    s = Solution()
    s.connect(tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4, 5, 6, 7]))
