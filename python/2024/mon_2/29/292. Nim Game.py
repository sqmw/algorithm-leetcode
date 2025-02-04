class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        题目理解有问题
        实际上是，每个人都在走最好的一步，题目要求是
            1. 其实目前到我的时候，只要此时 n 是 4 的整数倍，那么另外一个人就能让你永远都是 4 的整数倍
            2. 当自己的事 4 的时候，必输
        """
        I_can_win: bool = False
        can_finish: bool = False

        def recurse_win(surplus: int, now_is_me: bool):
            nonlocal I_can_win, can_finish
            if can_finish or surplus < 0:
                return
            if surplus < 4:
                if now_is_me:
                    I_can_win = True
                    can_finish = True
                return
            for val in range(1, 4):
                recurse_win(surplus - val, not now_is_me)

        recurse_win(n, True)

        return I_can_win


if __name__ == "__main__":
    s = Solution()
    print(s.canWinNim(8))  # False
