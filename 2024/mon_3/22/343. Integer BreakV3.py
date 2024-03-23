class Solution:
    def integerBreak(self, n: int) -> int:
        """
        T(n): O(1)
        S(n): O(1)
        """
        """
        通过观察我们可以发现，不能把 1 拆分出去
        3 * 3 > 2 * 2 * 2 > 6
        从 4 开始之后，每一个数字的拆分都比自己的 product 都比自己大

        如下拆分才能够得到最大的 product (这里是递归定义的)
        4 拆分成 2,3
        5 拆分成 2,3
        6 拆分成 2,3
        7 拆分成 2,3
        但是如果 出现了 3 * k == 2 * m的情况(k,m 分别表示3和2的数量)
        按照前面 3 * 3 > 2 * 2 * 2 (此时的 k 和 m 的关系一定是 2 和 3 之间的关系)，我们应该优先选择 3
        按照上面的思路，我们可以对动态规划递归方程进行优化
        """
        # 继续上面一个解法的思路
        # 我们可以对这个数字进行抽取 2 和 3
        quotient, remainder = divmod(n, 3)
        # 下面需要判定有几个 3，我们需要的事偶数个
        # remainder: [0, 2]
        if n < 4:
            return n - 1
        des_num = 0
        # 这里表示使用的是偶数个 3，余数是1的时候浪费了，除了 2, 3 必须有 1，其他的任何地方不能有 1
        if quotient % 2 == 0 and remainder != 1:
            des_num += (3 ** quotient)
        else:
            des_num += (3 ** (quotient - 1))
            remainder += 3

        if 1 < remainder < 5:
            des_num *= remainder
        elif remainder == 5:
            des_num *= 6
        return des_num


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(7))
