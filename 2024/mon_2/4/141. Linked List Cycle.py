from typing import Optional, Set

from util.core.list_util import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set: Set[ListNode] = set()
        p = head
        while p is not None:
            if p not in node_set:
                node_set.add(p)
            else:
                return True
            p = p.next
        return False
