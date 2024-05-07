class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        考察数学和思维的运用
        T(n): O(n ** 0.5)
        S(n: O(1)
        """
        if num <= 1:
            return False
        _sum: int = 1
        for val in range(2, int(num ** 0.5) + 1):
            if num % val == 0:
                print(val)
                _sum += (val + num // val)
        return _sum == num


if __name__ == "__main__":
    s = Solution()
    print(s.checkPerfectNumber(28))
