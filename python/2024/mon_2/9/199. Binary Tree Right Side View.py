from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        des_num_list: List[int] = []
        path: List[int] = []

        def preorder_r2l_traverse(_root: TreeNode):
            nonlocal des_num_list
            if _root is not None:
                if _root.left is None and _root.right is None:
                    if len(des_num_list) < len(path):
                        des_num_list += path[len(des_num_list):]
                if _root.right is not None:
                    path.append(_root.right.val)
                    preorder_r2l_traverse(_root.right)
                    path.pop()

                if _root.left is not None:
                    path.append(_root.left.val)
                    preorder_r2l_traverse(_root.left)
                    path.pop()

        if root is not None:
            path.append(root.val)
            preorder_r2l_traverse(root)
            path.pop()
        return des_num_list


if __name__ == "__main__":
    null = None
    print(Solution().rightSideView(tree_util.list2tree_breadth_first_traverse([1, 2])))
