from typing import List, Optional

from util.core.tree_util import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder_traverse(_root: Optional[TreeNode]):
            nonlocal des_num_list
            if _root is not None:
                des_num_list.append(_root.val)
                preorder_traverse(_root.left)
                preorder_traverse(_root.right)

        des_num_list: List[int] = []
        preorder_traverse(root)
        return des_num_list
