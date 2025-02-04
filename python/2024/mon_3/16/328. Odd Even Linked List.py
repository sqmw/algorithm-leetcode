# Definition for singly-linked list.
from typing import Optional

from python.util.core import list_util


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        T(n): O(n) # 量级刚好是 n
        S(n): O(1) # 仅仅使用了常数级的空间
        """
        if head is None or head.next is None:
            return head
        p = head
        # index 为奇数的 head
        odd_head: Optional[ListNode] = None
        # index 为奇数的 tail
        odd_last: Optional[ListNode] = None
        # index 为 偶数 的 tail
        even_last: Optional[ListNode] = None
        # 在这个过程中，让 p 一直指着 index 为 even 的ListNode
        while p is not None and p.next is not None:
            if odd_head is None:
                odd_head = p.next
                odd_last = odd_head
                even_last = head
                p.next = odd_last.next
                p = p.next

            else:
                odd_last.next = p.next
                odd_last = odd_last.next
                even_last = p
                p.next = odd_last.next
                if odd_last is not None:
                    p = odd_last.next
        if p is not None:
            even_last.next = p
            even_last = even_last.next
        even_last.next = odd_head
        odd_last.next = None
        return head


if __name__ == "__main__":
    s = Solution()
    print(list_util.list2arr(s.oddEvenList(list_util.arr2list([0, 1]))))
