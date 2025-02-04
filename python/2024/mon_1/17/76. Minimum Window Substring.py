"""
暴力？
超出时间限制
"""
import collections
import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def t_in_s(s2: str, start_s2, end_s2, t2: str, start_t2, end_t2) -> bool:
            """
            用来判断 t2 的每个字母能否在 s2 里面对应
            :param s2:
            :param start_s2:
            :param end_s2:
            :param t2:
            :param start_t2:
            :param end_t2:
            :return:
            """
            dic_t2 = {}
            dic_s2 = {}

            for i_t2 in range(start_t2, end_t2):
                if t2[i_t2] in dic_t2.keys():
                    dic_t2[t2[i_t2]] += 1
                else:
                    dic_t2[t2[i_t2]] = 1

            for i_s2 in range(start_s2, end_s2):
                if s2[i_s2] in dic_s2.keys():
                    dic_s2[s2[i_s2]] += 1
                else:
                    dic_s2[s2[i_s2]] = 1

            for k_t in dic_t2.keys():
                if k_t not in dic_s2 or dic_t2[k_t] > dic_s2[k_t]:
                    return False
            return True

        if not t_in_s(s, 0, len(s), t, 0, len(t)):
            return ''
        index = s.find(t)
        if index != -1:
            return s[index: index + len(t)]
        dic_t2 = collections.defaultdict(int)
        start = 0
        stop = 0
        for c_t in t:
            dic_t2[c_t] += 1
        init_dic = copy.copy(dic_t2)
        min_index_list = [0, len(s)]  # [)
        count = len(t)  # 用来表示还需要再s里面取的字符数量
        while stop <= len(s) and start < len(s):
            if count > 0 and stop < len(s):  # 表示还没有包含完
                stop += 1
                if s[stop - 1] in dic_t2.keys():
                    if dic_t2[s[stop - 1]] > 0:
                        count -= 1
                    dic_t2[s[stop - 1]] -= 1

            else:
                if count == 0 and min_index_list[1] - min_index_list[0] > stop - start:
                    min_index_list[0] = start
                    min_index_list[1] = stop
                if start < len(s):
                    start += 1
                    if s[start - 1] in dic_t2.keys():
                        if 0 <= dic_t2[s[start - 1]] < init_dic[s[start - 1]]:
                            count += 1
                        dic_t2[s[start - 1]] += 1
        return s[min_index_list[0]:min_index_list[1]]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("bba", "ab"))
