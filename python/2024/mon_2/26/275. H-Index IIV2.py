""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        T(n): O(log(n))
        S(n): O(1)
        需要注意边界条件
        这里直接得到结果
        """
        left = 0
        right = len(citations) - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1

        # return 0 if citations[0] == 0 else 1
        return len(citations) - left


if __name__ == "__main__":
    s = Solution()
    citations = [0]
    print(s.hIndex(citations))
