""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import random


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        T(n): O(log(n))
        S(n): O(1)
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) is True and isBadVersion(mid - 1) is False:
                return mid
            elif isBadVersion(mid) is True and isBadVersion(mid - 1):
                right = mid - 1
            else:
                left = mid + 1
