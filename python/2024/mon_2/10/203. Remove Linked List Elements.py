# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python.util.core import list_util
from python.util.core.list_util import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p_pre: Optional[ListNode] = None
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        else:
            p_pre = head
            while p_pre.next is not None:
                if p_pre.next.val == val:
                    p_pre.next = p_pre.next.next
                else:
                    p_pre = p_pre.next

        return head


if __name__ == "__main__":
    s = Solution()

    print(list_util.list2arr(s.removeElements(list_util.arr2list([1, 1, 1, 2, 3, 1, 1, 1, 1, 3, 4, 5, 6]), 1)))
