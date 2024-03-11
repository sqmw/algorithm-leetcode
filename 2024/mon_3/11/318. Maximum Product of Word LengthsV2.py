from typing import List, Set


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        method1:
            1. 构建一个List，里面存储每一个单词的 words[index] 的 26letter_mask_list
        T(n): O(n**2)
        S(n): O(n)
        """

        def word2mask(_word: str) -> int:
            _mask = 0
            for letter in _word:
                _mask |= 1 << (ord(letter) - 97)
            return _mask

        # T(n): O(words_len * word_len)
        words_mask_list: List[int] = [word2mask(word) for word in words]
        des_val = 0
        # 时间复杂度 O(words_len ** 2)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words_mask_list[i] & words_mask_list[j] == 0:
                    _len_product = len(words[i]) * len(words[j])
                    if _len_product > des_val:
                        des_val = _len_product
        return des_val


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
