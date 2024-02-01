class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        pre = 2
        pre_pre = 1
        now = 0
        for i in range(3, 1 + n):
            now = pre + pre_pre
            pre_pre = pre
            pre = now
        return now

    # 使用递归实现，时间复杂度完全不一样
    def climbStairs2(self, n: int) -> int:
        def climb(steps: int) -> int:
            if steps == 1:
                return 1
            elif steps == 2:
                return 2
            elif steps == 3:
                return 3
            else:
                return climb(steps - 1) + climb(steps - 2)

        return climb(n)


if __name__ == '__main__':
    s = Solution()
    steps = 40
    print(s.climbStairs(steps))
    print(s.climbStairs2(steps))
