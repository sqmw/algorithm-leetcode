#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        T(n): O(n)
        S(n): O(n)
        """
        if len(s) != len(t):
            return False
        char_dic: Dict[str: int] = {}
        for i in range(0, len(s)):
            if s[i] not in char_dic:
                char_dic[s[i]] = 0
            char_dic[s[i]] += 1
        for i in range(0, len(t)):
            try:
                char_dic[t[i]] -= 1
                if char_dic[t[i]] < 0:
                    return False
            except KeyError as e:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "aacc"
    t = "ccac"
    print(solution.isAnagram(s, t))
