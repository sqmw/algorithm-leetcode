from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        使用 hash 的方式来做(字母的数量是一个常数，并且字母的顺序是一定的，其实我们知道的常识一般也是有序的)
        T(n): O(n + m)
        S(n): O(1)
        :param s:
        :param t:
        :return:
        """
        s_hash_char_dic: List[int] = [0] * 26
        t_hash_char_dic: List[int] = [0] * 26
        for char in s:
            s_hash_char_dic[ord(char) - ord('a')] += 1

        for char in t:
            t_hash_char_dic[ord(char) - ord('a')] += 1

        for i in range(26):
            if s_hash_char_dic[i] != t_hash_char_dic[i]:
                return chr(i + ord('a'))


if __name__ == "__main__":
    solution = Solution()
    s = "abcd"
    t = "abcde"
    print(solution.findTheDifference(s, t))
