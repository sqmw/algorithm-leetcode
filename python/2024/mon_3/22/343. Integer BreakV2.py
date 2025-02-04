from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        T(n): O(n)
        S(n): O(n)
        """
        """
        通过观察我们可以发现，不能把 1 拆分出去(除了1-3是必须的)
        3 * 3 > 2 * 2 * 2 > 6
        从 4 开始之后，每一个数字的拆分都比自己的 product 都比自己大

        如下拆分才能够得到最大的 product (这里是递归定义的)
        4 拆分成 2,3
        5 拆分成 2,3
        6 拆分成 2,3
        7 拆分成 2,3
        但是如果 出现了 3 * k == 2 * m的情况
        按照前面 3 * 3 > 2 * 2 * 2 (此时的 k 和 m 的关系一定是 2 和 3 之间的关系)，我们应该优先选择 3
        按照上面的思路，我们可以对动态规划递归方程进行优化
        """
        if n < 4:
            return n - 1
        rec_f: List[int] = [i for i in range(n + 1)]
        if n >= 4:
            rec_f[4] = 4
        for i in range(4, n + 1):
            rec_f[i] = max(2 * rec_f[i - 2], 3 * rec_f[i - 3])
        return rec_f[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(10))
