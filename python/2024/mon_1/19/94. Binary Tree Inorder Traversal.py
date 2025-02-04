# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        des_arr: List[int] = []

        def inorder(_root: Optional[TreeNode]):
            if _root is None:
                return
            inorder(_root.left)
            des_arr.append(_root.val)
            inorder(_root.right)
        inorder(root)
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal())
