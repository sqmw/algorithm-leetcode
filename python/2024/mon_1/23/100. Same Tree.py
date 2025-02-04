from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(root1: TreeNode, root2):
            nonlocal is_same
            if not is_same:
                return
            if root1 is None and root2 is None:
                return
            elif (root1 is None and root2 is not None) or (root2 is None and root1 is not None) or (
                    root1.val != root2.val):
                is_same = False
            else:
                traverse(root1.left, root2.left)
                traverse(root1.right, root2.right)

        is_same = True
        traverse(p, q)
        return is_same


if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    print(s.isSameTree(tree_util.list2tree_breadth_first_traverse(arr1), tree_util.list2tree_breadth_first_traverse(arr2)))
