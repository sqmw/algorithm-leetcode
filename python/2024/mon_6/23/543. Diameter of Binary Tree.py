# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, Dict

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        T(n): O(nlog(n))
        S(n): O(nlog(n))
        计算二叉树的直径，实际上是中等难度的题目
        :param root:
        :return: int
        可以构造领接表然后遍历实现（方法比较简单）
        也可以直接遍历二叉树，遍历的过程中计算高度（可以是一次遍历，也可以是逐个遍历点）
        T(n): min = O(n)
        S(n): min = O(n)
        """
        des_diameter = 0
        # 表示的事深度
        depth_dic: Dict = collections.defaultdict(int)
        def dfs(_root: Optional[TreeNode]) -> int:
            nonlocal des_diameter
            """
            :param _root:
            :return: 返回通过该节点的 diameter
            """
            if _root is None:
                return 0
            dfs(_root.left)
            dfs(_root.right)
            depth_dic[_root] = 1 + max(depth_dic[_root.left], depth_dic[_root.right])
            des_diameter = max(des_diameter, depth_dic[_root.left] + depth_dic[_root.right])
            return depth_dic[_root.left] + depth_dic[_root.right]
        dfs(root)
        return des_diameter


if __name__ == "__main__":
    null = None
    s = Solution()
    print(s.diameterOfBinaryTree(tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4])))
