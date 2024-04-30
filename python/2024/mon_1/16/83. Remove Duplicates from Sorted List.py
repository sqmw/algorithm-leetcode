# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from python.util.core import list_util
from python.util.core.list_util import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = head
        if head is None or head.next is None:
            return head
        p = head.next
        while p is not None:
            if p.val != pre_node.val:
                pre_node.next = p
                pre_node = p
                p = p.next
            elif p.next is None:
                pre_node.next = None
                break
            else:
                p = p.next

        return head


if __name__ == '__main__':
    s = Solution()
    l_head = ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3)))))))
    print(list_util.list2arr(s.deleteDuplicates(l_head)))
