from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """
        method: 逆序求解
            将表达式拆分开来计算即可
            (x * y) mod m == ((x mod m) * (y mod m)) m # 这个是一个递归定义，并且具有累计效果
        """
        MOD = 1337
        t = a
        res = 1
        for i in range(len(b) - 1, -1, -1):
            res = res * pow(t, b[i], MOD)
            t = (t ** 10) % MOD
        return res % MOD


if __name__ == "__main__":
    s = Solution()
    print(s.superPow(133, [1, 2, 2, 4, 5, 5, 6, 7, 8, 8]))
