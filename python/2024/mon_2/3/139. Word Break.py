from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        先决条件：既然 wordDict 是一个dictionary 那么任何一个唯一
        性能很不稳定
        上一个版本的做法本身不合理，因为把 word_dict 作为了操作对象
        :param s:
        :param wordDict:
        :return:
        """
        word_dict_set = set(wordDict)

        def recurse_break(start_index):
            nonlocal can_break
            if start_index == len(s):
                can_break = True
            for i in range(1, len(s) - start_index + 1):
                if can_break:
                    return
                if s[start_index: start_index + i] in word_dict_set:
                    recurse_break(start_index + i)

        can_break = False
        recurse_break(0)
        return can_break


if __name__ == "__main__":
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd"]

    print(Solution().wordBreak(s, wordDict))
