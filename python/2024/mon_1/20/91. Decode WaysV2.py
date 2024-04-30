"""
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
使用traceback方法时间很长，很慢，时间不能通过
"""
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        使用动态规划（迭代/数学归纳）实现
        "11106" can be mapped into:
        "AAJF" with the grouping (1 1 10 6)
        "KJF" with the grouping (11 10 6)
        f(n) = f(n - 1) + f(n - 2) # f(n-1) # 两个都有效的时候，两个都加，否则仅仅加一个，或者不能通过(无效的使用0)
        """
        # 判断是否可解码，不可以就返回0
        if len(s) == 0 or s[0] == '0' or s.find('00') != -1 or len(s)>1 and s[1] == '0' and int(s[0]) > 2:
            return 0

        f: List[int] = [0 for _ in range(len(s))]
        f[0] = 1
        if len(s) == 1:
            return 1
        else:
            if s[1] == '0':
                f[1] = 1
            else:
                f[1] = 1
                if 1 <= int(s[0] + s[1]) <= 26:
                    f[1] += 1
        i = 2
        if len(s) > 2 and s[2] == '0':
            if int(s[1] + s[2]) > 26 or int(s[1] + s[2]) < 1:
                return 0
            f[2] = f[0]
            f[1] = f[0]
            i += 1
        while i < len(s):
            combine = i + 1 <= len(s) - 1 and s[i + 1] == '0'
            if combine and (int(s[i] + s[i + 1]) > 26 or int(s[i] + s[i + 1]) < 1):
                return 0
            if s[i - 1] == '0':
                f[i] = f[i - 2]
                i += 1
            elif s[i] == '0' or not (1 <= int(s[i - 1] + s[i]) <= 26):
                f[i] = f[i - 1]
                i += 1
            elif combine and 1 <= int(s[i] + s[i + 1]) <= 26:
                f[i] = f[i - 1]
                f[i + 1] = f[i - 1]
                i += 2
            else:
                f[i] = f[i - 1] + f[i - 2]
                i += 1
        return f[len(s) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("12"))
