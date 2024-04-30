import math
from typing import List


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        使用动态规划思想
        T(n): O(n/1 + n/2 + n/3 + n/4 + n/5 + ... + n/n) == O(nlog(n))
        S(n): O(n)
        """
        return int(math.sqrt(n))


if __name__ == "__main__":
    s = Solution()
    print(s.bulbSwitch(9999999))
