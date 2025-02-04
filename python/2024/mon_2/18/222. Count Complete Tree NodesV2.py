from typing import Optional

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        通过遍历每一个节点得到数量
        T(n): O(log(n)**2)
        S(n): O(h)[可以不使用递归就能降低到O(1)，但是没必要]
        """

        def get_node_count(_root) -> int:
            if _root.left is None:
                return 1
            height_left = get_height(_root.left)
            height_right = get_height(_root.right)
            if height_left == height_right:
                return (1 << height_left) + get_node_count(_root.right)
            else:
                return (1 << height_right) + get_node_count(_root.left)

        def get_height(_root: Optional[TreeNode]) -> int:
            height = 0
            while _root is not None:
                height += 1
                _root = _root.left
            return height

        count = get_node_count(root)
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countNodes(tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4, 5])))
