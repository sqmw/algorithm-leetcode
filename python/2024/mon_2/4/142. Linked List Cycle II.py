from typing import Optional, Set

from python.util.core.list_util import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        通过 hashSet 实现
        :param head:
        :return:
        """
        node_set: Set[ListNode] = set()
        p = head
        while p is not None:
            if p in node_set:
                return p
            else:
                node_set.add(p)
            p = p.next
        return None
