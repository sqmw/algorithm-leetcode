from typing import Optional

from util.core import list_util
from util.core.list_util import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        """
        通过修改指针实现，思想为选择排序，把小于x的提到左边来
        :param head:
        :param x:
        :return:
        """
        count = 0
        list_len = 0
        q = head
        while q is not None:
            list_len += 1
            if q.val < x:
                count += 1
            q = q.next
        if count == 0 or count == list_len:
            return head
        if head.val >= x:
            q = head
            while True:
                if q.next.val < x:
                    m = q.next
                    q.next = q.next.next
                    m.next = head
                    head = m
                    break
                else:
                    q = q.next
        count -= 1
        # p 以及其之前的节点都是满足条件 <= x
        p = head
        while count > 0:
            q = p.next
            if p.next.val >= x:
                while True:
                    if q.next is not None:
                        if q.next.val < x:
                            m = q.next
                            q.next = q.next.next

                            m.next = p.next
                            p.next = m
                            break
                        else:
                            q = q.next
                    else:
                        break
            p = p.next
            count -= 1
        return head


if __name__ == '__main__':
    s = Solution()
    _my_list = s.partition(list_util.arr2list([2, 0, 4, 1, 3, 1, 4, 0, 3]), 4)
    print(list_util.list2arr(_my_list))
