import random
from typing import Optional, List

from python.util.core import list_util
from python.util.core.list_util import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        归并排序
        :param head:
        :return:
        """
        if head is None:
            return None
        node_list: List[ListNode] = []
        p = head
        while p is not None:
            node_list.append(p)
            p = p.next
        node_list.sort(key=lambda node: node.val)
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[len(node_list) - 1].next = None
        return node_list[0]


if __name__ == "__main__":
    print(list_util.list2arr(Solution().sortList(list_util.arr2list([random.randint(1, 1000) for _ in range(100)]))))
