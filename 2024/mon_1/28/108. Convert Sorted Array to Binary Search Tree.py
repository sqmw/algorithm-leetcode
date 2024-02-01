import math
from typing import List, Optional

from util.core.tree_util import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        实现方法有点类似归并排序
        :param nums:
        :return:
        """
        root: Optional[TreeNode] = TreeNode(nums[int((len(nums) - 1) / 2)])

        # 设置孩子
        def recurse2set_children(_root: TreeNode, root_index, start_index: int, stop_index: int):
            """
            [start_index, param stop_index):
            :param root_index:
            :param stop_index:
            :param start_index:
            :param _root:
            :return:
            """
            if stop_index - start_index == 2:
                _root.right = TreeNode(nums[start_index + 1])
            elif stop_index - start_index <= 1:
                return
            else:
                _root.left = TreeNode(nums[int((start_index + root_index - 1) / 2)])
                recurse2set_children(_root.left, int((start_index + root_index - 1) / 2), start_index, root_index)
                _root.right = TreeNode(nums[int((root_index + 1 + stop_index - 1) / 2)])
                recurse2set_children(_root.right, int((root_index + 1 + stop_index - 1) / 2), root_index + 1,
                                     stop_index)

        recurse2set_children(root, int((len(nums) - 1) / 2), 0, len(nums))
        return root


if __name__ == '__main__':
    s = Solution()
    tree = s.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7])
    print(tree)
