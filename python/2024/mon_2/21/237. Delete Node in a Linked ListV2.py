#!/usr/bin/python
# -*- coding: utf-8 -*-

from python.util.core import list_util


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        T(n): O(1)
        S(n): O(1)

        通过把数字都向前移动一个位置、然后删除最后一个节点
        """
        now_next = node.next
        node.val = now_next.val
        node.next = now_next.next


if __name__ == "__main__":
    s = Solution()
    sq_list = list_util.arr2list([1, 2, 3, 4, 5, 6])
    p = sq_list
    while p is not None:
        if p.val == 2:
            break
        p = p.next
    s.deleteNode(p)
    print(list_util.list2arr(sq_list))
