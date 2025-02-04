from python.util.core.list_util import *


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        p = head
        # position = index + 1
        position = 1
        pre: ListNode = ListNode()
        tail: ListNode = ListNode()
        mid: ListNode = ListNode()
        tail_pre: ListNode = ListNode()
        while position <= right + 1:
            if p:
                next_p = p.next
            if position == left - 1:
                pre = p
            elif position == right + 1:
                tail = p
            if left <= position <= right:
                if left == position:
                    mid = p
                    tail_pre = p
                else:
                    t = p
                    t.next = mid
                    mid = t
            p = next_p
            position += 1
        if left != 1:
            pre.next = mid
            tail_pre.next = tail
        else:
            tail_pre.next = tail
            head = mid
        return head


if __name__ == '__main__':
    s = Solution()
    print(list2arr(s.reverseBetween(arr2list([1, 2, 3, 4, 5]), 1, 2)))
