from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        val_list: List[int] = []

        def get_val_list(_root: Optional[TreeNode]):
            if _root is None:
                return
            get_val_list(_root.left)
            val_list.append(_root.val)
            get_val_list(_root.right)

        get_val_list(root)
        wrong_val1 = wrong_val2 = float('-inf')

        for i in range(0, len(val_list)):
            if wrong_val1 == float('-inf') and i + 1 < len(val_list) and val_list[i] > val_list[i + 1]:
                wrong_val1 = val_list[i]
            if i > 0 and val_list[i] < val_list[i - 1]:
                wrong_val2 = val_list[i]

        def get_wrong_parent(_root: Optional[TreeNode]):
            if _root is None:
                return
            if _root.val == wrong_val1:
                _root.val = wrong_val2
            elif _root.val == wrong_val2:
                _root.val = wrong_val1
            get_wrong_parent(_root.left)
            get_wrong_parent(_root.right)

        get_wrong_parent(root)


if __name__ == '__main__':
    s = Solution()
    tree = tree_util.list2tree_breadth_first_traverse([1, 3, None, None, 2])
    s.recoverTree(tree)
    print(tree_util.tree2list_pre_traverse(tree))
