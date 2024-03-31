class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s from t
        使用双指针实现
        T(n): O(n + m)
        S(n): O(1)
        """
        if s == '':
            return True
        s_i = 0
        t_i = 0
        while s_i < len(s) and t_i < len(t):
            while True:
                if s_i >= len(s):
                    return True
                if t_i >= len(t):
                    break
                if s[s_i] != t[t_i]:
                    t_i += 1
                else:
                    t_i += 1
                    s_i += 1
            s_i += 1

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence(s="b", t="abc"))
