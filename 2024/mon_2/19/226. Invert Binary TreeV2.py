from typing import Optional

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        method1： 反向拷贝
        T(n): O(n)
        S(n): O(n)
        method2： 方向逆转
        T(n): O(n)
        S(n): O(h)[实际上是递归的深度(O(h))]
        """
        if root is None:
            return None

        def preorder_traverse(_root: Optional[TreeNode]):
            if _root is not None:
                t = _root.left
                _root.left = _root.right
                _root.right = t
                preorder_traverse(_root.left)
                preorder_traverse(_root.right)

        preorder_traverse(root)
        return root


if __name__ == "__main__":
    s = Solution()
    print(tree_util.tree2list_pre_traverse(
        s.invertTree(tree_util.list2tree_breadth_first_traverse([4, 2, 7, 1, 3, 6, 9]))))
