from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        """
        T(n): O(n)
        S(n): O(n) # O(1) 为最小，此时使用动态规划
        """
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n - 2)


if __name__ == "__main__":
    s = Solution()
    print(s.fib(40))