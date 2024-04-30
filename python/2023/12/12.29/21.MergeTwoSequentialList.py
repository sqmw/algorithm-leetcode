# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        newHead = None
        p = list1
        q = list2
        if list1.val < list2.val:
            newHead = list1
            p = p.next
        else:
            newHead = list2
            q = q.next
        tail = newHead
        while True:
            if q is None:
                tail.next = p
                return newHead
            elif p is None:
                tail.next = q
                return newHead
            else:
                if p.val < q.val:
                    tail.next = p
                    tail = p
                    p = p.next
                else:
                    tail.next = q
                    tail = q
                    q = q.next


if __name__ == '__main__':
    s = Solution()
    t = s.mergeTwoLists(ListNode(1, ListNode(2)), ListNode(1, ListNode(3)))
    l: list[int] = []
    while t is not None:
        l.append(t.val)
        t = t.next
    print(l)
