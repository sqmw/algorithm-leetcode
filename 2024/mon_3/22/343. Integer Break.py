import math
from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        显然需要使用动态规划来实现
        显然 n >= 2
        T(n): O(n**2)
        S(n): O(n)
        """
        if n < 3:
            return 1
        rec_f: List[int] = [1 for _ in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(2, math.ceil(i / 2) + 1):
                rec_f[i] = max(rec_f[i], max(j, rec_f[j]) * max(i - j, rec_f[i - j]))
        return rec_f[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(3))
