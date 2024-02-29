from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        先决条件：既然 wordDict 是一个dictionary 那么任何一个唯一
        :param s:
        :param wordDict:
        :return:
        """
        wordDict.sort(key=lambda key: len(key))
        i = 0
        while i < len(wordDict):
            if s.find(wordDict[i]) == -1:
                del wordDict[i]
            else:
                i += 1
        # 给wordDict去除多余的
        # i = 1
        # while i < len(wordDict):
        #     if self.wordBreak(wordDict[i], wordDict[0: i]):
        #         del wordDict[i]
        #     else:
        #         i += 1

        # tuple: [start, end)
        word_dict_tuple_list: List[tuple] = []
        for word in wordDict:
            start = 0
            index = s.find(word, start)
            while index != -1:
                word_dict_tuple_list.append((index, index + len(word)))
                start = index + 1
                index = s.find(word, start)

        word_dict_tuple_list.sort(key=lambda item: item[0])

        def recurse_to_find(now_index, need_val):
            nonlocal can_break
            if can_break or need_val == 0:
                can_break = True
                return
            for i in range(now_index, -1, -1):
                if word_dict_tuple_list[i][1] == need_val:
                    recurse_to_find(i - 1, word_dict_tuple_list[i][0])
                elif word_dict_tuple_list[i][1] < need_val:
                    return

        can_break = False

        if len(word_dict_tuple_list) > 0 and word_dict_tuple_list[len(word_dict_tuple_list) - 1][1] == len(s):
            recurse_to_find(len(word_dict_tuple_list) - 1, len(s))
        return can_break


if __name__ == "__main__":
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd"]

    print(Solution().wordBreak(s, wordDict))
