from typing import List, Set


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        method1:
            1. 构建一个List，里面存储每一个单词的 letter 的 set_list
        T(n): O(n**2)
        S(n): O(n)
        """
        # 时间复杂度: O(nlog(n))
        # words.sort(reverse=True, key=lambda word: (len(word), word))

        # T(n): O(words_len * word_len)
        words_set_list: List[Set] = [set() for _ in range(len(words))]
        for i in range(len(words)):
            for char in words[i]:
                words_set_list[i].add(char)
        des_val = 0
        # 时间复杂度 O(words_len ** 2)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len((words_set_list[i] & words_set_list[j])) == 0:
                    _len_product = len(words[i]) * len(words[j])
                    if _len_product > des_val:
                        des_val = _len_product
        return des_val


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
