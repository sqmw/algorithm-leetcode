from typing import Optional

from util.core import tree_util
from util.core.tree_util import TreeNode

null = None


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        height_dic: dict = {}

        is_balance: bool = True

        def recurse_to_limit(_root: Optional[TreeNode]):
            nonlocal is_balance
            if _root is None:
                return
            else:
                recurse_to_limit(_root.left)
                recurse_to_limit(_root.right)
                if is_balance is False:
                    return

                if _root.val == 2:
                    print(2)
                if _root.left is None and _root.right is None:
                    height_dic[_root] = 1
                elif _root.left is not None and _root.right is None:
                    if height_dic[_root.left] > 1:
                        is_balance = False
                        return
                    height_dic[_root] = height_dic[_root.left] + 1
                elif _root.right is not None and _root.left is None:
                    if height_dic[_root.right] > 1:
                        is_balance = False
                        return
                    height_dic[_root] = height_dic[_root.right] + 1
                else:
                    print(_root.val)
                    if abs(height_dic[_root.left] - height_dic[_root.right]) > 1:
                        is_balance = False
                        return
                    else:
                        height_dic[_root] = max(height_dic[_root.left], height_dic[_root.right]) + 1
                print(height_dic[_root], _root.val)
        recurse_to_limit(root)
        return is_balance


if __name__ == "__main__":
    s = Solution()
    res = s.isBalanced(tree_util.list2tree_breadth_first_traverse([1,2,2,3,null,null,3,4,null,null,4]))
    print(res)
