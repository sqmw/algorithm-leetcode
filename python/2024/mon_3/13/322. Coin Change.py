from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        使用回溯法枚举
        T(n): O(amount**coins)
        S(n): O(coins)
        超时
        """

        def traceback():
            nonlocal need, des_cou, now_cou
            if need == 0:
                if des_cou == -1 or des_cou > now_cou:
                    des_cou = now_cou
            if need < 0:
                return
            for coin in coins:
                need -= coin
                now_cou += 1
                traceback()
                need += coin
                now_cou -= 1

        need: int = amount
        des_cou = -1
        now_cou = 0
        traceback()
        return des_cou


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
