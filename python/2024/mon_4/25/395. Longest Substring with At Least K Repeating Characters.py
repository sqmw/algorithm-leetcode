class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        下面的代码没有实现完全
        似乎 T(n) == O(n ** 2) 也能通过的
        采用分治、hash、滑动窗口
            0 1 2 3 4 5 6 ... len - 1
        a
        b
        c
        d
        d
        T(n): O(n) # 实际上是 O(26 * n)
        S(n): O(n) # 实际上是 O(26 * n)
        """
        cou_matrix = [[0 for _ in range(len(s))] for _ in range(26)]
        # 统计出每个字符到目前为止的出现的次数
        for i in range(len(s)):
            if i > 0:
                cou_matrix[ord(s[i]) - ord('a')][i] = cou_matrix[ord(s[i]) - ord('a')][i - 1] + 1
            else:
                cou_matrix[ord(s[i]) - ord('a')][i] = 1
            for j in range(i + 1, len(s)):
                cou_matrix[ord(s[i]) - ord('a')][j] = cou_matrix[ord(s[i]) - ord('a')][j - 1]
        # 使用贪心思想，往前可能更好的时候
        # 两个都是包含
        # 如果 right 往前 能够让右边
        left = 0
        right = len(s) - 1

        def find_max(_left: int, _right: int) -> int:
            # 找到其中一个在区间 [_left, _right] 不符合条件的
            ...

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubstring('defababbcd', 2))
