from typing import Dict, List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        T(n): O(n)
        S(n): O(n)
        目前没有对空间进行常数比例减少降低复杂度
        :param s:
        :param t:
        :return:
        """
        chr_last_appear_index_dic: Dict[str, int] = dict()
        s_last_appear_index: List[int] = []
        t_last_appear_index: List[int] = []
        for i in range(len(s)):
            if s[i] in chr_last_appear_index_dic:
                s_last_appear_index.append(chr_last_appear_index_dic[s[i]])
            else:
                chr_last_appear_index_dic[s[i]] = i
                s_last_appear_index.append(-1)

        chr_last_appear_index_dic = dict()
        for i in range(len(t)):
            if t[i] in chr_last_appear_index_dic:
                t_last_appear_index.append(chr_last_appear_index_dic[t[i]])
            else:
                chr_last_appear_index_dic[t[i]] = i
                t_last_appear_index.append(-1)

        return t_last_appear_index == s_last_appear_index


if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = "avv"
    print(solution.isIsomorphic(s, t))
