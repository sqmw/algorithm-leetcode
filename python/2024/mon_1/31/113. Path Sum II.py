from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

null = None

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        des_path_list: List[List[int]] = []
        path: List[int] = []

        def traceback(_root: Optional[TreeNode]):
            nonlocal targetSum
            if _root.left is None and _root.right is None and targetSum == 0:
                des_path_list.append(path[:])
            else:
                if _root.left is not None:
                    targetSum -= _root.left.val
                    path.append(_root.left.val)
                    traceback(_root.left)
                    path.pop()
                    targetSum += _root.left.val

                if _root.right is not None:
                    targetSum -= _root.right.val
                    path.append(_root.right.val)
                    traceback(_root.right)
                    path.pop()
                    targetSum += _root.right.val

        targetSum -= root.val
        path.append(root.val)
        traceback(root)
        path.pop()
        targetSum += root.val

        return des_path_list


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(tree_util.list2tree_breadth_first_traverse([]), 0))
