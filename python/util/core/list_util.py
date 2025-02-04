from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2arr(l: ListNode) -> List:
    des_arr = []
    p = l
    while p is not None:
        des_arr.append(p.val)
        p = p.next
    return des_arr


def arr2list(arr: List) -> Optional[ListNode]:
    if len(arr) == 0:
        return None
    else:
        head = ListNode(arr[0])
        p = head
        for i in range(1, len(arr)):
            p.next = ListNode(arr[i])
            p = p.next
    return head
