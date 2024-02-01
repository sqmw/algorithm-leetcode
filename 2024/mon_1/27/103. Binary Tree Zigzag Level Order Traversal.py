from typing import Optional, List

from util.core import tree_util
from util.core.tree_util import TreeNode

null = None


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l2r = True
        des_nums_list: List[List[int]] = []
        _queue: List[TreeNode] = [root]
        while len(_queue) > 0:
            level_len = len(_queue)
            level_num: List[int] = []
            for i in range(level_len):
                node = _queue[0]
                del _queue[0]
                if node is not None:
                    level_num.append(node.val)
                    _queue.append(node.left)
                    _queue.append(node.right)
            if l2r is not True:
                level_num.reverse()
            des_nums_list.append(level_num)
            l2r = not l2r

        del des_nums_list[len(des_nums_list) - 1]
        return des_nums_list


if __name__ == '__main__':
    s = Solution()
    print(s.zigzagLevelOrder(tree_util.list2tree_breadth_first_traverse([1, 2, 3, 4, None, None, 5])))
