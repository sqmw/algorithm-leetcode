class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        T(n): O(n)
        S(n): O(1)
        """
        _all_lowercase: bool = True
        _all_higher: bool = True
        _only_first: bool = False
        # 对于第一个字母，先不处理
        for i in range(1, len(word)):
            char = word[i]
            if not ord('a') <= ord(char) <= ord('z'):
                _all_lowercase = False
            if not ord('A') <= ord(char) <= ord('Z'):
                _all_higher = False
        # 判断是否仅仅首字母大写的
        if ord('A') <= ord(word[0]) <= ord('Z') and _all_lowercase:
            _only_first = True

        if not ord('a') <= ord(word[0]) <= ord('z'):
            _all_lowercase = False
        if not ord('A') <= ord(word[0]) <= ord('Z'):
            _all_higher = False

        return _all_higher or _all_lowercase or _only_first


if __name__ == "__main__":
    s = Solution()
    print(s.detectCapitalUse("FlaG"))
