import collections
from typing import List, Dict, Set


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        T(n): O(n)
        S(n): O(1)
        """
        # 构建 row_dict
        letter_row_dic: Dict[str, int] = collections.defaultdict(int)
        for letter in "qwertyuiop":
            letter_row_dic[letter] = 0
        for letter in "asdfghjkl":
            letter_row_dic[letter] = 1
        for letter in "zxcvbnm":
            letter_row_dic[letter] = 2
        des_str_list: List[str] = []
        for word in words:
            lowercase_word = word.lower()
            diff_set: Set[int] = set()
            # 判断当前的 word 组成的 letter 来自哪些行
            for letter in lowercase_word:
                diff_set.add(letter_row_dic[letter])

            if len(diff_set) == 1:
                des_str_list.append(word)

        return des_str_list


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
