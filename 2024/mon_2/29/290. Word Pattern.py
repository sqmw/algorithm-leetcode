from typing import List, Dict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true
        思路1：分别给 pattern 和 s 进行编码(编码从1开始，使用了hash字典)
            pattern : 1221
            s:        1221
            T(n): O(n)
            S(n): O(n)
            最低使用一个循环即可得到两个字符串的编码
        思路2：后看法，就是看当前的char的编码上次出现的位置，这样就可以得到一个数组，类似floyd算法
            S(n) == O(len(set(pattern)))
        """
        # dict中的int用来表示编号范围为 1,2,3,4...
        coding_dic: Dict[str, int] = dict()
        pattern_coding: List[int] = []
        s_coding: List[int] = []
        now_val = 1
        for char in pattern:
            if char not in coding_dic:
                coding_dic[char] = now_val
                now_val += 1
            pattern_coding.append(coding_dic[char])

        now_val = 1
        s_word_list = s.split(' ')
        coding_dic = dict()
        for word in s_word_list:
            if word not in coding_dic:
                coding_dic[word] = now_val
                now_val += 1
            s_coding.append(coding_dic[word])
        # print(s_coding)

        return len(pattern_coding) == len(s_coding) and pattern_coding == s_coding


if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(solution.wordPattern(pattern, s))
