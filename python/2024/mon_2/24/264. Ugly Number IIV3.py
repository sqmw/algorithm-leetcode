""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import heapq
from typing import List, Set


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        T(n): (nlog(n))
        S(n): O(n)
        因为构成的因素是2,3,5
            1. 从<5>开始的数后面的数字一定是前面的数字的乘积
            2. 采用三指针
        """
        if n <= 6:
            return n
        heap = [1]
        diff_set: Set = set()
        times = 0
        val_235 = [2, 3, 5]
        while times < n - 1:
            popped = heapq.heappop(heap)
            times += 1
            for item in val_235:
                if popped * item not in diff_set:
                    diff_set.add(popped * item)
                    heapq.heappush(heap, popped * item)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(1350))
    # for i in range(1, 1350):
    #     print(i, s.nthUglyNumber(i))
