from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        通过 preorder_traverse + backtrack 实现
        :param root:
        :return:
        """
        total_sum = 0
        path: List[int] = []

        def traceback(_root: Optional[TreeNode]):
            nonlocal total_sum
            nonlocal path
            # 表示现在的节点是叶子节点
            if _root.left is None and _root.right is None:
                print(path)
                for i in range(len(path) - 1, -1, -1):
                    total_sum += path[i] * 10 ** (len(path) - 1 - i)
            if _root.left is not None:
                path.append(_root.left.val)
                traceback(_root.left)
                path.pop()

            if _root.right is not None:
                path.append(_root.right.val)
                traceback(_root.right)
                path.pop()

        if root is not None:
            path.append(root.val)
            traceback(root)
            path.pop()
        return total_sum


if __name__ == "__main__":
    print(Solution().sumNumbers(tree_util.list2tree_breadth_first_traverse([])))
