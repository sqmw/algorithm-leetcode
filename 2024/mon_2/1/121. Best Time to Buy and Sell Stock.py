from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
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
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
