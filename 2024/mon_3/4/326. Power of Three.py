class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                return False
        return n == 1


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(5))
