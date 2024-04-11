class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        实际难度: 中等
        T(n): O(n)
        S(n): O(1)
        """

        t_s = s * 2
        return t_s.find(s, 1, len(t_s) - 1) != -1


if __name__ == "__main__":
    s = Solution()
    #  {'a': [0, 2, 3, 5, 7, 8, 10, 12, 13], 'b': [1, 4, 6, 9, 11, 14]}
    # abaab
    print(s.repeatedSubstringPattern("abaababaababaa"))
