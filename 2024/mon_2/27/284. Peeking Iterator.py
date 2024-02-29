""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from ctypes import Union


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    """
    1. 定义属性 val_cur_next
    2. 让 val_cur_next 一直等于 iterator 的 cur 的 next 值
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.t: Iterator = iterator
        self.val_cur_next: [int, None] = self.t.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.val_cur_next

    def next(self):
        """
        :rtype: int
        """
        des_val: int = self.val_cur_next
        if self.t.hasNext():
            self.val_cur_next = self.t.next()
        else:
            self.val_cur_next = None
        return des_val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.val_cur_next is None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
