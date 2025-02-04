from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

null = None


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        通过递归实现先序遍历，通过循环实现的话，可能占用的内存小一点
        t: O(n)
        s: O(1)
        """
        pre: Optional[TreeNode] = None

        # 通过该函数得到的是左边全是孩子的，需要修改为右边全是孩子的
        def preorder_traverse(_root: TreeNode):
            nonlocal pre
            if _root is None:
                return
            if pre is not None:
                pre.left = _root
                pre = _root
                print(_root.val)
            else:
                pre = _root
            preorder_traverse(_root.left)
            preorder_traverse(_root.right)

        preorder_traverse(root)

        # 将全是左孩子修改为全是右孩子
        p = root
        while p is not None:
            p.right = p.left
            temp = p
            p = p.left
            temp.left = None


if __name__ == '__main__':
    s = Solution()
    tree = tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4, 5, 6, 7, 8, 9])
    s.flatten(tree)
    print('')
