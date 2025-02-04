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
        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and i < len(s) and s[i] == ' ':
                    i += 1
            else:
                # 走到当前的 segment 的结尾
                while i < len(s) and s[i] != ' ':
                    i += 1
                segment_cou += 1
        return segment_cou


if __name__ == "__main__":
    s = Solution()
    print(s.countSegments(" Hello,    my name is John "))
