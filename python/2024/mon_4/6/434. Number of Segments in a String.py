class Solution:
    def countSegments(self, s: str) -> int:
        """
        :param s:
        :return:
        T(n): O(n)
        S(n): O(1)
        """
        segment_cou = 0
        i = 0
        s = s.strip(' ')
        while i < len(s):
            # 每次开始都让 s[i] 是一个 非 space 字符
            while i < len(s) and i < len(s) and s[i] == ' ':
                i += 1
            # 走到当前的 segment 的结尾
            while i < len(s) and s[i] != ' ':
                i += 1
            segment_cou += 1
        return segment_cou


if __name__ == "__main__":
    s = Solution()
    print(s.countSegments(" Hello,    my name is John "))
