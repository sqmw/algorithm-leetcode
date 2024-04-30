""" 需要指定编码的时候解开这个注释
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        """
        T(n): O(log(n))
        S(n): O(1)
        """
        if n == 1:
            return True
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(4))
