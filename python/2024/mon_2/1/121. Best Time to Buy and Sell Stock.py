from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        method: 使用动态规划实现，和官方题解不一样
        实际难度： 中等
        T(n): O(n)
        S(n): O(1)
        :param prices:
        :return:
        """
        pre = 0
        _max = 0
        for i in range(1, len(prices)):
            now = max(prices[i] - prices[i - 1], pre + prices[i] - prices[i - 1])
            pre = now
            if now > _max:
                _max = now
        return max(_max, 0)


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 2, 5, 3, 6, 4]))
