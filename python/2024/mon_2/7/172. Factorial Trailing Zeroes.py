import collections
from typing import Set, Dict


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        dic52: Dict[int, int] = collections.defaultdict(lambda: 0)
        trail_zero_cou: int = 0

        def recurse2zero():
            nonlocal val
            nonlocal trail_zero_cou
            nonlocal dic52
            if val % 10 == 0:
                trail_zero_cou += 1
                val = int(val / 10)
                recurse2zero()
            if val % 2 == 0:
                if dic52[5] > 0:
                    trail_zero_cou += 1
                    dic52[5] -= 1
                else:
                    dic52[2] += 1
                val = int(val / 2)
                recurse2zero()
            if val % 5 == 0:
                if dic52[2] > 0:
                    trail_zero_cou += 1
                    dic52[2] -= 1
                else:
                    dic52[5] += 1
                val = int(val / 5)
                recurse2zero()

        val: int = 0
        for i in range(1, n + 1):
            val = i
            recurse2zero()
        return trail_zero_cou


if __name__ == "__main__":
    print(Solution().trailingZeroes(10000))
