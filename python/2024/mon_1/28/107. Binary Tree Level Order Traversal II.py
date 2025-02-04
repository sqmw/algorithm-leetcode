from typing import Optional, List

from python.util.core import tree_util
from python.util.core.tree_util import TreeNode

null = None


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        _queue: List[TreeNode] = [root]
        des_nums_arr: List[List[int]] = []
        while len(_queue) > 0:
            level_nums: List[int] = []
            level_len = len(_queue)
            for i in range(level_len):
                node = _queue[0]
                del _queue[0]
                if node is not None:
                    level_nums.append(node.val)
                    _queue.append(node.left)
                    _queue.append(node.right)
            des_nums_arr.append(level_nums)

        del des_nums_arr[len(des_nums_arr) - 1]
        des_nums_arr.reverse()
        return des_nums_arr


if __name__ == '__main__':
    s = Solution()
    print(s.levelOrderBottom(tree_util.list2tree_breadth_first_traverse([3, 9, 20, null, null, 15, 7])))

