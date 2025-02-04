class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        实际难度: 中等
        T(n): O(n**2)
        S(n): O(1)
        """

        def pre_next_same(start, gap) -> bool:
            for i in range(gap):
                if s[start + i] != s[start + i - gap]:
                    return False

            return True

        # base_cou 表示的是可以构成 s 的substring的长度
        for base_cou in range(1, len(s) // 2 + 1):
            if len(s) % base_cou == 0:
                # 判定是否在整个 s 里面都能够适合
                can_fit = True
                for i in range(base_cou, len(s), base_cou):
                    if not pre_next_same(i, base_cou):
                        can_fit = False
                        break
                if can_fit:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    #  {'a': [0, 2, 3, 5, 7, 8, 10, 12, 13], 'b': [1, 4, 6, 9, 11, 14]}
    # abaab
    print(s.repeatedSubstringPattern("abaab abaab abaab"))
