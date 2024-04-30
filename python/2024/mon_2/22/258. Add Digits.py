class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = num % 10 + num // 10
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(38))
