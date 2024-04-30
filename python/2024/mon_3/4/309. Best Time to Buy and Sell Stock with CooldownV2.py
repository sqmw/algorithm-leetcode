from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        """
        if not prices:
            return 0
        # 每一天的状态只能是 hold(持有)、sell(要卖)、cooldown(冷却)
        n = len(prices)
        # hold[i]：第i天持有股票所得的最大利润
        hold = [0] * n

        # sell[i]：第i天卖出股票所得的最大利润
        sell = [0] * n

        # cooldown[i]：第i天处于冷却状态所得的最大利润
        cooldown = [0] * n

        hold[0] = -prices[0]  # 第一天只能买股票
        sell[0] = 0  # 第一天不可能卖股票
        cooldown[0] = 0  # 第一天不可能冷却

        for i in range(1, n):
            hold[i] = max(hold[i - 1], cooldown[i - 1] - prices[i])
            sell[i] = hold[i - 1] + prices[i]
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])
        return max(sell[n - 1], cooldown[n - 1])  # 返回最后一天卖出或冷却的最大利润


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
