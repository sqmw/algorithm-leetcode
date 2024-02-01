# Definition for singly-linked list.
from typing import Optional

from util.core import list_util
from util.core.list_util import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 0
        p = head
        if head is None or head.next is None or k == 0:
            return head
        while p is not None:
            list_len += 1
            p = p.next
        k = k % list_len
        if k == 0:
            return head
        now_index = 1
        p = head
        while now_index < list_len - k:
            p = p.next
            now_index += 1
        q = p.next
        p.next = None
        p = q
        while q.next is not None:
            q = q.next
        q.next = head
        return p


if __name__ == '__main__':
    s = Solution()
    print(list_util.list2arr(s.rotateRight(None, 3)))
