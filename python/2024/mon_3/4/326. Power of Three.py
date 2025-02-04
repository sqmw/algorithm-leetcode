class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        这里的 base 3 是一个质数，因此只能是它组成别人，不能是别人组成他
        """
        if n <= 0:
            return False

        return 3486784401 % n == 0 and (3486784401 // n) % 3 == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(5))
