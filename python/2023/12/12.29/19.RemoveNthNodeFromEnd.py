# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        p = head
        while p is not None:
            len_list += 1
            p = p.next
        if len_list == 0 or (len_list == 1 and n == 1):
            return None
        if n == len_list:
            head = head.next
            return head
        current_index = 1
        p = head
        while current_index < len_list - n + 1 - 1:
            p = p.next
            current_index += 1
        p.next = p.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print(s.removeNthFromEnd(l1, 1))
    print(1)
