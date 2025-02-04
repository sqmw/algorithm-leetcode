""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List, Set


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        T(n): (O(n),O(n**2)),猜测时间复杂度是O(nlog(n))
        S(n): O(n)
        因为构成的因素是2,3,5
            1. 从<5>开始的数后面的数字一定是前面的数字的乘积
            2. 采用三指针
        """
        rec_f: List[int] = [i + 1 for i in range(5)]
        if n <= 5:
            return rec_f[n - 1]
        index_2 = 1
        index_3 = 1
        index_5 = 1
        while len(rec_f) < n:
            while rec_f[index_2] * 2 <= rec_f[-1]:
                index_2 += 1
            while rec_f[index_3] * 3 <= rec_f[-1]:
                index_3 += 1
            while rec_f[index_5] * 5 <= rec_f[-1]:
                index_5 += 1
            val_min = min(2 * rec_f[index_2], 3 * rec_f[index_3], 5 * rec_f[index_5])
            if val_min == 2 * rec_f[index_2]:
                index_2 += 1
            elif val_min == 3 * rec_f[index_3]:
                index_3 += 1
            elif val_min == 5 * rec_f[index_5]:
                index_5 += 1
            rec_f.append(val_min)

        return rec_f[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(1350))
    # for i in range(1, 1350):
    #     print(i, s.nthUglyNumber(i))
