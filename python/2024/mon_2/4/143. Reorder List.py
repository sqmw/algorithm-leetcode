from typing import Dict

from python.util.core.list_util import *


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        S(n): O(n)
        T(n): O(n)
        """
        index_node_dic: Dict[int, ListNode] = {}
        index = 0
        p = head
        while p is not None:
            index_node_dic[index] = p
            p = p.next
            index += 1
        for i in range(int(index / 2)):
            index_node_dic[i].next = index_node_dic[index - 1 - i]

            index_node_dic[index - 1 - i].next = index_node_dic[i + 1]
        index_node_dic[int(index / 2)].next = None


if __name__ == '__main__':
    l: Optional[ListNode] = arr2list([1, 2, 3, 4, 5])
    Solution().reorderList(l)
    print(list2arr(l))
