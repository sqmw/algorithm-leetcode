from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

null = None


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            # 按照逻辑板来讲，这里应该在 target == 0的时候返回 True，其他时候返回False
            return False
        need: int = targetSum
        has = False

        def traceback(_root: TreeNode):
            nonlocal need, has

            if _root.left is None and _root.right is None and need == 0:
                has = True
                return
            if _root is None or has:
                return
            if _root.left is not None:
                need -= _root.left.val
                traceback(_root.left)
                need += _root.left.val
            if _root.right is not None:
                need -= _root.right.val
                traceback(_root.right)
                need += _root.right.val
        need -= root.val
        traceback(root)
        need += root.val

        return has


if __name__ == '__main__':
    s = Solution()
    print(
        s.hasPathSum(tree_util.list2tree_breadth_first_traverse([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]), 22))
