import collections
import sys
from typing import Dict


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        分治、递归、逆向动态规划、cache
        :param n:
        :return:
        """
        cache: Dict[tuple, int] = collections.defaultdict(int)

        def cache_dp(start: int, stop: int) -> int:
            """
            [start, stop]
            :param start:
            :param stop:
            :return:
            """
            if start >= stop:
                return 0
            if (start, stop) in cache:
                return cache[(start, stop)]
            now_miniMax = sys.maxsize
            for _root_val in range(start, stop + 1):
                now = _root_val + max(cache_dp(start, _root_val - 1), cache_dp(_root_val + 1, stop))
                now_miniMax = min(now_miniMax, now)
            cache[(start, stop)] = now_miniMax
            return now_miniMax
        cache_dp(1, n)
        return cache[(1, n)]


if __name__ == "__main__":
    s = Solution()
    print(s.getMoneyAmount(16))
