from typing import Optional, Set

from util.core.list_util import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headA_ref_set: Set[ListNode] = set()
        p = headA
        while p is not None:
            headA_ref_set.add(p)
            p = p.next
        p = headB
        while p is not None:
            if p in headA_ref_set:
                return p
            p = p.next
        return None
