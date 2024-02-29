from typing import Optional

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        T(n): O(k)
        S(n): O(min(k, h))
        """

        def preorder(_root: Optional[TreeNode]):
            nonlocal des_val
            if _root is not None and des_val is None:
                preorder(_root.left)

                nonlocal now_k
                now_k += 1
                if now_k == k:
                    des_val = _root.val

                preorder(_root.right)

        des_val: Optional[int | None] = None
        now_k = 0
        preorder(root)
        return des_val


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(tree_util.list2tree_breadth_first_traverse([3, 1, 4, None, 2]), 4))
