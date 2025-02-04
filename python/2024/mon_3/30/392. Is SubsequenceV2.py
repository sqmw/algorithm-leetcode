import collections


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s from t
        m: t_lena
        n: s_len
        这里使用类似动态规划的思想实现
        T(n): O(m * 26)
        S(n): O(m * 26)
        """
        if s == '':
            return True
        if len(s) > len(t):
            return False
        # 最开始的出现位置是 len(t) 表示都没有出现过
        init_row = [len(t)] * 26
        matrix: collections.deque = collections.deque()
        for i in range(len(t) - 1, -1, -1):
            init_row[ord(t[i]) - ord('a')] = i
            matrix.appendleft(init_row.copy())
        last_row_index = 0
        for i in range(len(s)):
            print(matrix[i][ord(s[i]) - ord('a')])
            if last_row_index >= len(t) or matrix[last_row_index][ord(s[i]) - ord('a')] >= len(t):
                return False
            last_row_index = matrix[last_row_index][ord(s[i]) - ord('a')] + 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence(s="acb", t="ahbgdc"))
