import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        method1:
            本质是求解二次方程，并且向下取整
        T(n): O(1) # 本质是 log(n)，数字的相加的时间复杂度不是简单的 O(1)
        S(n): O(1)
        1 -> 1 == 1 : (1 + 1) * 1 / 2
            2
        2 -> 1 + 2 == 3 : (1 + 2) * 2 / 2
            4 5
        3 -> 1 + 2 + 3 == 6 : (1 + 3) * 3 / 2
            7 8 9
        4 -> 1 + 2 + 3 + 4 == 10: (1 + 4) * 4 / 2
        """
        candidate = ((1 + 8 * n) ** 0.5 - 1) / 2
        return math.floor(candidate)


if __name__ == "__main__":
    s = Solution()
    print(s.arrangeCoins(8))
