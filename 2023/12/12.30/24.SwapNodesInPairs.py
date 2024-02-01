# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 长度为 0 或者 1， 直接返回
        if head is None or head.next is None :
            return head
        p = head
        q = head
        while p is not None:
            # 表示现在是操作头结点
            if q == head:
                head = q.next
                p = q.next.next
                q.next.next = q
                q.next = p

                p = head.next
            else:
                # 表示不够交换
                if p is None or p.next is None or p.next.next is None:
                    return head
                else:
                    q = p.next
                    p.next = q.next
                    q.next = p.next.next
                    p.next.next = q

                    p = q

        return head


if __name__ == '__main__':
    s = Solution()
    a = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    arr = []
    while a is not None:
        arr.append(a.val)
        a = a.next
    print(arr)
