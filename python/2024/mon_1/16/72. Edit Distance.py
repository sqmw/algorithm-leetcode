"""
word1 -> word2

难度: 难
"""
from typing import List, Union


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0 or len2 == 0:
            return len1 + len2
        f = [[0 for _ in range(len1)] for _ in range(len2)]
        for i in range(len1):
            if word1.find(word2[0], 0, i + 1) != -1:
                f[0][i] = i
            else:
                f[0][i] = i + 1
        for i in range(len2):
            if word2.find(word1[0], 0, i + 1) != -1:
                f[i][0] = i
            else:
                f[i][0] = i + 1
        for i in range(1, len2):
            for j in range(1, len1):
                if word2[i] == word1[j]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i][j - 1] + 1, f[i - 1][j] + 1, f[i - 1][j - 1] + 1)
        return f[len2 - 1][len1 - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('horse', 'ros'))
