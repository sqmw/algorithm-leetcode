from typing import Optional, List

from util.core.tree_util import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        t: O(n)
        s: O(n)
        :param root:
        :return:
        """
        des_arr_list: List[List[int]] = []
        _queue: List[TreeNode] = [root]
        level_list: List[int] = []
        while len(_queue) > 0:
            _level_len = len(_queue)
            level_list.clear()
            for i in range(_level_len):
                node = _queue[0]
                del _queue[0]
                if node is not None:
                    level_list.append(node.val)
                    _queue.append(node.left)
                    _queue.append(node.right)
            des_arr_list.append(level_list[:])
        del des_arr_list[len(des_arr_list) - 1]
        return des_arr_list
