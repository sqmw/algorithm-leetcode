from typing import Optional, List

from util.core import tree_util
from util.core.tree_util import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        通过循环加栈实现，性能较低，需要微调
        :param root:
        :return:
        """
        if root is None:
            return True
        visited_node: List[TreeNode] = []

        tree_nodes: List[TreeNode] = [root]
        value_list: List[int] = []
        _root = root

        while len(tree_nodes) > 0:
            # 左孩子
            if _root.left is not None and _root.left not in visited_node:
                tree_nodes.append(_root.left)
            # 右孩子
            else:
                visited_node.append(_root)
                value_list.append(_root.val)
                tree_nodes.pop()

                if _root.right is not None:
                    if _root.right not in visited_node:
                        tree_nodes.append(_root.right)
            if len(tree_nodes) > 0:
                _root = tree_nodes[len(tree_nodes) - 1]
        for i in range(1, len(value_list)):
            if value_list[i - 1] >= value_list[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(tree_util.list2tree_breadth_first_traverse([5, 1, 4, None, None, 3, 6])))
