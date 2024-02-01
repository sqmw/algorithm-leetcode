import sys
from typing import Optional, List

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        通过循环加队列实现
        :param root:
        :return:
        """
        if root is None:
            return True

        last_val = -sys.maxsize
        _root = root
        valid = True

        def inorder(_root):
            nonlocal valid
            nonlocal last_val
            if _root is None or valid is False:
                return
            else:
                inorder(_root.left)
                if last_val >= _root.val:
                    valid = False
                else:
                    last_val = _root.val
                inorder(_root.right)

        inorder(root)
        return valid


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(tree_util.list2tree_breadth_first_traverse([5, 1, 4, None, None, 3, 6])))
