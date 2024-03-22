class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        T(n): O(n**0.5)
        S(n): O(1)
        """
        i = 1
        while i ** 2 < num:
            i += 1
        return i ** 2 == num


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(23))
