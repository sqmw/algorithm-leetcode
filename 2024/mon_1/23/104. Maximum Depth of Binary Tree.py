from typing import Optional

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        使用了traceback实现
        :param root:
        :return:
        """
        _max_depth = 0
        _now_depth = 0
        if root is None:
            return 0

        def traceback(_root):
            nonlocal _now_depth
            nonlocal _max_depth
            if _root is None:
                return
            else:
                _now_depth += 1
                _max_depth = max(_max_depth, _now_depth)
                traceback(_root.left)
                _now_depth -= 1

                _now_depth += 1
                _max_depth = max(_max_depth, _now_depth)
                traceback(_root.right)
                _now_depth -= 1

        traceback(root)
        return _max_depth


if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(tree_util.list2tree_breadth_first_traverse([1, None, 2])))
