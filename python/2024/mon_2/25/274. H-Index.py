""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        T(n): O(nlog(n))
        S(n): O(1)
        思路：
             1. 升序排序
             2. 从后往前进行判定，从后到前包括当前的数字的数量，如果当前的数字 >=cou ，则当前的cou符合条件
             3. 一旦发现有一个数字不符合条件，就跳出循环
        """
        citations.sort()
        for i in range(len(citations) - 1, -1, -1):
            # 最小次数 >= 长度
            if citations[i] >= len(citations) - i:
                continue
            else:
                return len(citations) - i - 1
        # 意思是上面的 else 没有执行，上面的每一个数字都通过了题目条件
        return len(citations)


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([1]))
