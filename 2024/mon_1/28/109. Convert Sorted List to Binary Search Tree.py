from typing import Optional, List

from util.core.list_util import ListNode
from util.core.tree_util import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        method1: 这里我借用了108题目实现 时间复杂度 T(n) = O(log(n) + n) = O(n)
        method2: 不使用数组的话，每一次加入一个时间复杂度为 T(n) = O(log(1) + log(2) + ... + log(n))
        :param head:
        :return:
        """
        nums: List[int] = []
        while head is not None:
            nums.append(head.val)
            head = head.next

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

        root: Optional[TreeNode] = TreeNode(nums[int((len(nums) - 1) / 2)])
        recurse2set_children(root, int((len(nums) - 1) / 2), 0, len(nums))
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.sortedListToBST())
