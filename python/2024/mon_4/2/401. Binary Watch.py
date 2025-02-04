import collections
from typing import List, Dict


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 实际难度 中等中间
        """
        H: 仅仅能选择 0-3 -> 4个
        M: 选择的范围是 0-5 -> 6个 (全满表示的事 63 不符合题目要求)

        method1: 打表全部的选择情况，将对应 turnedOn 的筛选出来，时间复杂度很低[T(n) < 12 * 60]，
                 但是有点缺乏思考了(但是对于需要频繁进行执行 turnOn 这个操作的实际情况，性能会有明显提升)
        method2: 根据 turnOn 的选择情况，每次选择一个，得到排列数字，时间复杂度可以接受

        # 这里的 k 实际上是一个常数
        T(n): O(n * k)
        S(n): O(k)

        H: h8 h4 h2 h1
        M: m32 m16 m8 m4 m2 m1

        """

        def traceback(surplus: int, now_start):
            nonlocal now_m_set

            if surplus < 0:
                return
            # 表示现在取够了
            elif surplus == 0:
                if sum(now_m_set) < 60:
                    # 得到符合要求的 m_set
                    # print(h_cou_dic[turnedOn - len(now_m_set)], now_m_set)
                    for h in h_cou_dic[turnedOn - len(now_m_set)]:
                        des_str_arr.append(f'{h}:' + f'{sum(now_m_set)}'.rjust(2, '0'))
                return
            for m_index in range(now_start, len(m_list)):
                if m_list[m_index] not in now_m_set:
                    now_m_set.add(m_list[m_index])
                    traceback(surplus - 1, m_index + 1)
                    now_m_set.discard(m_list[m_index])

        h_cou_dic: Dict[int, List[int]] = collections.defaultdict(list)
        h_cou_dic[0] = [0]
        h_cou_dic[1] = [8, 4, 2, 1]
        h_cou_dic[2] = [10, 9, 6, 5, 3]
        h_cou_dic[3] = [11, 7]
        m_list = [32, 16, 8, 4, 2, 1]
        now_m_set = set()
        des_str_arr: List[str] = []
        h_max = 3
        m_max = 5
        if turnedOn > h_max + m_max:
            return []
        # 得到 h_m 的划分
        for h_cou in range(0, 4):
            m_cou = turnedOn - h_cou
            if m_cou > m_max or m_cou < 0:
                continue
            print(h_cou, m_cou)
            # 根据 m_cou 得到 m_set
            traceback(m_cou, 0)
        return des_str_arr


if __name__ == "__main__":
    s = Solution()
    print(s.readBinaryWatch(7))
