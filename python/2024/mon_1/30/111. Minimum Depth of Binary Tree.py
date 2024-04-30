import sys
from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

null = None


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        method1: 使用回溯法实现
        method2: 也可以使用循环加上一个 _queue 实现
        :param root:
        :return:
        """
        if root is None:
            return 0
        min_depth = sys.maxsize
        now_depth = 1

        def traceback2min(_root: TreeNode):
            if _root is None:
                return
            nonlocal min_depth
            nonlocal now_depth, min_depth
            if _root.left is None and _root.right is None:
                min_depth = min(min_depth, now_depth)
            now_depth += 1
            traceback2min(_root.left)
            now_depth -= 1

            now_depth += 1
            traceback2min(_root.right)
            now_depth -= 1

        traceback2min(root)

        return min_depth


if __name__ == '__main__':
    s = Solution()
    print(s.minDepth(tree_util.list2tree_breadth_first_traverse([2, null, 3, null, 4, null, 5, null, 6])))
