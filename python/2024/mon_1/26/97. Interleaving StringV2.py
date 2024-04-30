import copy
from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        前置条件 len(s1) + len(s2) = len(s3)
        这里使用的是贪心算法，但是实际上，贪心算法在这里并不收敛
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if s3 == '':
            return True
        m = n = 0
        is_interleave = False
        index_s1 = index_s2 = index_s3 = 0
        while index_s3 <= len(s3):
            sub_len_s1 = sub_len_s2 = 0
            for i in range(0, len(s3) - index_s3 + 1):
                index = s1.find(s3[index_s3: index_s3 + i + 1], index_s1)
                if index == -1 or index != index_s1 or i == len(s3) - index_s3:
                    sub_len_s1 = i
                    break
            for i in range(0, len(s3) - index_s3 + 1):
                index = s2.find(s3[index_s3: index_s3 + i + 1], index_s2)
                if index == -1 or index != index_s2 or i == len(s3) - index_s3:
                    sub_len_s2 = i
                    break
            if sub_len_s1 == sub_len_s2 == 0:
                break
            # 此时截取 s1
            if sub_len_s1 > sub_len_s2:
                n += 1
                index_s1 += sub_len_s1
                index_s3 += sub_len_s1
            # 此时截取 s2
            else:
                m += 1
                index_s2 += sub_len_s2
                index_s3 += sub_len_s2
            if index_s3 >= len(s3):
                is_interleave = True
        if abs(m - n) > 1 or (n == 0 and s1 != '') or (m == 0 and s2 != ''):
            is_interleave = False
        return is_interleave


if __name__ == '__main__':
    s = Solution()
    s1 = "a"
    s2 = ""
    s3 = "a"
    print(s.isInterleave(s1, s2, s3))
