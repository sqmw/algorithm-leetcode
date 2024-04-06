import collections
from typing import Dict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        :param s:
        :return:
        method1: 使用 hash 实现
        T(n): O(n)
        S(n): O(1)
        """
        have_odd = False
        letter_arr_dic: Dict[str, int] = collections.defaultdict(int)
        for letter in s:
            letter_arr_dic[letter] += 1
        des_cou = 0
        for v in letter_arr_dic.values():
            if v % 2 == 1:
                have_odd = True
            des_cou += (v // 2) * 2
        return des_cou + 1 if have_odd else des_cou


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
