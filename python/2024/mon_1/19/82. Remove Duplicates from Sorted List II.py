from typing import Optional

from python.util.core import list_util
from python.util.core.list_util import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 首先解决空条件可长度仅仅是 1 的

        temp = head
        while head.next.val == head.val:
            while head is not None and head.next is not None and head.val == head.next.val:
                head = head.next
            if temp.val == temp.next.val:
                head = head.next
            if head is None or head.next is None:
                return head
        """
        时间复杂度 O(n)
        :param head:
        :return:
        """
        # 首先解决空条件可长度仅仅是 1 的
        if head is None or head.next is None:
            return head
        p: ListNode
        q: ListNode = head
        while q is not None and q.val == head.val:
            p = q
            q = q.next
        while q is not None and q.next is not None:
            if q.next is not None:
                if q.val == q.next.val:
                    t = q.next
                    while not (t.next is None or t.next.val != q.val):
                        t = t.next
                    p.next = t.next
                    q = t.next
                else:
                    p = q
                    q = q.next
        return head



if __name__ == '__main__':
    s = Solution()
    _my_list = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))
    _my_list = s.deleteDuplicates(_my_list)
    print(list_util.list2arr(_my_list))
