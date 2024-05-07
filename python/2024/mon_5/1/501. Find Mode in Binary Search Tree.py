# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional, List, Dict

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        使用先序遍历
        T(n): O(n)
        S(n): O(distinct_val)
        """
        cou_dic: Dict[int, int] = collections.defaultdict(int)

        def pre_traverse(_root: Optional[TreeNode]):
            nonlocal cou_dic
            if _root is None:
                return
            # 先序遍历，进行统计
            cou_dic[_root.val] += 1
            pre_traverse(_root.left)
            pre_traverse(_root.right)

        pre_traverse(root)

        # 在遍历右边的节点之前，统计一下前面出现的
        _max_cou = max(cou_dic.values())
        _new_dic = collections.defaultdict(int)
        for k, v in cou_dic.items():
            if v == _max_cou:
                _new_dic[k] = v
        cou_dic = _new_dic

        return [k for k in cou_dic.keys()]


if __name__ == "__main__":
    s = Solution()
    print(s.findMode(tree_util.list2tree_breadth_first_traverse([1, 0, 1, 0, 0, 1, 1, 0])))
