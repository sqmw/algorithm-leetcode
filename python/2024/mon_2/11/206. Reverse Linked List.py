from typing import Optional

from python.util.core import list_util
from python.util.core.list_util import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        now_head: ListNode = head
        p: ListNode = head.next
        now_head.next = None
        while p is not None:
            p_next = p.next
            p.next = now_head
            now_head = p
            p = p_next

        return now_head


if __name__ == "__main__":
    s = Solution()
    print(list_util.list2arr(s.reverseList(list_util.arr2list([1, 2, 3, 4, 5]))))
