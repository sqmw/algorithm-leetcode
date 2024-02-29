from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划实现，递推
        :param prices:
        :return:
        """
        _max_profit = 0
        now_index_before_max = [0 for _ in range(len(prices))]
        for i in range(1, len(now_index_before_max)):
            if prices[i] - prices[i - 1] > 0:
                now_index_before_max[i] = now_index_before_max[i - 1] + prices[i] - prices[i - 1]
            else:
                now_index_before_max[i] = now_index_before_max[i - 1]
        return now_index_before_max[len(now_index_before_max) - 1]


if __name__ == "__main__":
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
