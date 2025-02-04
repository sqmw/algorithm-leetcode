""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        T(n): O(n**2)
        S(n): O(1)
        """
        for i in range(len(citations), -1, -1):
            if i <= sum([ele >= i for ele in citations]):
                return i
        # 意思是上面的 else 没有执行，上面的每一个数字都通过了题目条件
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3, 3, 3, 3]))
