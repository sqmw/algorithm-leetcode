""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
from typing import List, Set


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        使用hash set理论上
        T(n): O(n**x)
        S(n): O(n)
        S(n) 可以优化为 O(n)
        严重超时
        """
        rec_f: List[int] = [i + 1 for i in range(5)]
        if n <= 5:
            return rec_f[n - 1]

        dis_set: Set = set(rec_f)
        now_len = 5
        now_val = 5
        while now_len < n:
            now_val += 1
            if now_val % 2 == 0 and now_val // 2 in dis_set:
                dis_set.add(now_val)
                now_len += 1
            elif now_val % 3 == 0 and now_val // 3 in dis_set:
                dis_set.add(now_val)
                now_len += 1
            elif now_val % 5 == 0 and now_val // 5 in dis_set:
                dis_set.add(now_val)
                now_len += 1

        return now_val


if __name__ == "__main__":
    s = Solution()
    # print(s.nthUglyNumber(1350))
    for i in range(1, 1350):
        print(i, s.nthUglyNumber(i))
