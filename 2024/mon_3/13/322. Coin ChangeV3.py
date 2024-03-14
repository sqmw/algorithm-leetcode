import math
import sys
from typing import List, Set


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T(n): O(n*cou_coin)
        S(n): O(n)
        这个代码是对上次的代码的优化
        """
        # rec_f[i] 表示的事 amount_i 需要的兑换数量
        rec_f: List[int] = [sys.maxsize] * (amount + 1)
        rec_f[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                rec_f[i] = min(rec_f[i], rec_f[i - coin] + 1)

        return rec_f[amount] if rec_f[amount] != sys.maxsize else -1


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([156, 265, 40, 280], 9109))
