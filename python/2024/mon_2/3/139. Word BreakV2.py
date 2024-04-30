from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        T(n): O(n)
        S(n): O(n)
        :param s:
        :param wordDict:
        :return:
        """
        word_dict_set = set(wordDict)
        dp: List[bool] = [False] * (len(word_dict_set) + 1)
        dp[0] = True
        for i in range(1, len(word_dict_set) + 1):
            for j in range(0, i):
                if dp[j] and s[j: i]:
                    dp[i] = True

        return dp[len(word_dict_set)]


if __name__ == "__main__":
    s = "a"
    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]

    print(Solution().wordBreak(s, wordDict))
