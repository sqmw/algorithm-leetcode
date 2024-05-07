import collections
from typing import Optional, List, Dict

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        使用后序遍历，要想达到空间复杂度的效果是 O(1)
        1. 每次遍历每一个子树的时候，看该子树的 child_val 和 父节点的 parent_val
        2. 如果不相同，就传入一个<新的><空的> dict, 后序遍历回来父节点，统计数字进行处理
        T(n): O(n)
        S(n): O(1)
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
