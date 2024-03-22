import collections
from typing import Optional, Dict

from util.core.tree_util import TreeNode, list2tree_breadth_first_traverse


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        每一个节点都有 max_rob,从叶子结点开始，因此需要使用后续遍历，
        保证每一个节点在访问的时候都已经访问过了他的孩子节点
        T(n): O(n)
        S(n): O(n)
        """
        sub_tree_rob_max_dic: Dict[TreeNode, int] = collections.defaultdict(int)

        def get_now_tree_max(_root) -> int:
            """
            这里的分类讨论比较麻烦//当时脑子不太清醒，想错了，这里仅仅一个分类讨论而已
            """
            candidate_a: int = 0
            candidate_b: int = 0
            # 没有 _root 参与
            candidate_a = (sub_tree_rob_max_dic[_root.left] + sub_tree_rob_max_dic[_root.right])
            # 有 _root 参与
            candidate_b = (_root.val +
                           sub_tree_rob_max_dic[getattr(_root.left, 'left', None)] +
                           sub_tree_rob_max_dic[getattr(_root.left, 'right', None)] +
                           sub_tree_rob_max_dic[getattr(_root.right, 'left', None)] +
                           sub_tree_rob_max_dic[getattr(_root.right, 'right', None)])
            return candidate_a if candidate_a > candidate_b else candidate_b

        def recurse_traverse(_root: Optional[TreeNode]):
            if _root is None:
                return
            recurse_traverse(_root.left)
            recurse_traverse(_root.right)
            # print(_root.val)
            sub_tree_rob_max_dic[_root] = get_now_tree_max(_root)

        recurse_traverse(root)

        return sub_tree_rob_max_dic[root]


if __name__ == "__main__":
    null = None
    s = Solution()
    print(s.rob(list2tree_breadth_first_traverse([10, 5, 15, 1, 8, null, 7])))
