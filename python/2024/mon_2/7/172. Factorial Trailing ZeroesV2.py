import collections
from typing import Set, Dict


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        trail_zero_cou: int = 0

        for i in range(5, n + 1):
            if i % 5 == 0:
                while i % 5 == 0:
                    trail_zero_cou += 1
                    i /= 5

        return trail_zero_cou


if __name__ == "__main__":
    print(Solution().trailingZeroes(10000))
