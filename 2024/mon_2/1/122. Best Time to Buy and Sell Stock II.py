from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划实现，递推
        以后做动态规划需要写出递推公式
        :param prices:
        :return:
        """
        _max_profit = 0
        pre = now = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                now = pre + prices[i] - prices[i - 1]
            else:
                now = pre
            pre = now
        return now


if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
