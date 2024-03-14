import math
import sys
from typing import List, Set


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        使用动态规划
        T(n): O(n**2)
        S(n): O(n)
        超时
        """
        # rec_f[i]: 表示的是 amount_i 需要的 coin 数量
        if amount == 0:
            return 0
        coins_set: Set[int] = set(coins)
        rec_f: List[int] = [0] * (amount + 1)
        for i in range(1, amount + 1):
            if i in coins_set:
                rec_f[i] = 1
            else:
                need_min = sys.maxsize
                for j in range(1, math.ceil(i / 2) + 1):
                    if rec_f[j] + rec_f[i - j] < need_min and rec_f[j] > 0 and rec_f[i - j] > 0:
                        need_min = rec_f[j] + rec_f[i - j]
                rec_f[i] = need_min

        return rec_f[-1] if rec_f[-1] != sys.maxsize and rec_f[-1] != 0 else -1


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5, 20], 100))
