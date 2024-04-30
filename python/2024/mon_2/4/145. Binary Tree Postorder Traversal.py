from typing import Optional, List

from python.util.core.tree_util import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder_traverse(_root: Optional[TreeNode]):
            nonlocal des_num_list
            if _root is not None:
                postorder_traverse(_root.left)
                postorder_traverse(_root.right)
                des_num_list.append(_root.val)

        des_num_list: List[int] = []
        postorder_traverse(root)

        return des_num_list
