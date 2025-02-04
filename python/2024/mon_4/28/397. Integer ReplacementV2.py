import collections
from typing import Dict


class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        method1:
            使用动态规划,记忆化搜索
            T(n): O(log(n))
            S(n): O(log(n))
        method2:
            使用贪心算法求解
            T(n): O(log(n))
            S(n): O(1)
            对于每一个数字
            # 此时表示 n 为偶数
            if n % 2 == 0:
                n //= 2
            # 此时表示 n 为基数
            if n % 2 == 1:
                显然 n % 4 的余数只能是 1 或者 3
                当余数是 1 的时候，我们需要 -1
                当余数是 3 的时候，我们需要 +1

                # 但是 3 是一个特殊的数字, 需要 3 - 1

        这里使用了 method2
        """
        cou: int = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                remainder_four = n % 4
                if n == 3 or remainder_four == 1:
                    n -= 1
                else:
                    n += 1
            cou += 1

        return cou


if __name__ == "__main__":
    s = Solution()
    print(s.integerReplacement(7))
