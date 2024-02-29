class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        题目理解有问题
        实际上是，每个人都在走最好的一步，题目要求是
            1. 其实目前到我的时候，只要此时 n 是 4 的整数倍，那么另外一个人就能让你永远都是 4 的整数倍
            2. 当自己的事 4 的时候，必输
        """
        if n % 4 == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    print(s.canWinNim(8))  # False
