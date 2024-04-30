from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        l_right2left: List[Optional[TreeNode]] = []
        r_left2right: List[Optional[TreeNode]] = []
        l_right2left.append(root.left)
        r_left2right.append(root.right)

        while len(l_right2left) > 0:
            if l_right2left[0] is None and r_left2right[0] is None:
                del r_left2right[0]
                del l_right2left[0]
                continue
            elif (l_right2left[0] is None and r_left2right[0] is not None) or (
                    l_right2left[0] is not None and r_left2right[0] is None):
                return False
            elif l_right2left[0].val != r_left2right[0].val:
                return False
            # 表示两个的值相等
            else:
                r_left2right.append(r_left2right[0].left)
                r_left2right.append(r_left2right[0].right)
                del r_left2right[0]

                l_right2left.append(l_right2left[0].right)
                l_right2left.append(l_right2left[0].left)
                del l_right2left[0]

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isSymmetric(tree_util.list2tree_breadth_first_traverse([1, 2, 2, 3, 4, 4, 3])))
