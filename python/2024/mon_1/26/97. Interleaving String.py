import copy
from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3 == '':
            return True
        """
        1、回溯法，题目描述有问题(+超出时间限制)
        2、***读错题目了
        :param s1:
        :param s2:
        :param s3:
        :return:
        """

        def traceback():
            nonlocal next_start_index_s1
            nonlocal next_start_index_s2
            nonlocal next_start_index_s3
            nonlocal is_interleave
            nonlocal last_s1_index, last_s2_index
            nonlocal s3_chr_bind, des_s3_chr_bind

            if is_interleave:
                return

            index = s1.find(s3[next_start_index_s3], next_start_index_s1)
            if index != -1:
                s3_chr_bind.append(1)

                if index > last_s1_index + 1:
                    last_s1_index = index
                if next_start_index_s3 == len(s3) - 1:
                    is_interleave = True
                    des_s3_chr_bind = copy.deepcopy(s3_chr_bind)
                    return

                next_start_index_s3 += 1
                last_next_index = next_start_index_s1
                next_start_index_s1 = index + 1
                traceback()
                next_start_index_s3 -= 1
                next_start_index_s1 = last_next_index
                s3_chr_bind.pop()
            index = s2.find(s3[next_start_index_s3], next_start_index_s2)
            if index != -1:

                s3_chr_bind.append(2)

                if index > last_s2_index + 1:
                    last_s1_index = index
                if next_start_index_s3 == len(s3) - 1:
                    des_s3_chr_bind = copy.deepcopy(s3_chr_bind)
                    is_interleave = True
                    return

                next_start_index_s3 += 1
                last_next_index = next_start_index_s2
                next_start_index_s2 = index + 1

                traceback()
                next_start_index_s3 -= 1
                next_start_index_s2 = last_next_index
                s3_chr_bind.pop()

        is_interleave = False
        next_start_index_s1: int = 0
        next_start_index_s2: int = 0
        next_start_index_s3: int = 0

        last_s1_index = last_s2_index = -2
        n = m = 0
        s3_chr_bind: List[int] = []
        des_s3_chr_bind: List[int] = []
        traceback()

        if is_interleave:
            if des_s3_chr_bind[0] == 1:
                n += 1
            else:
                m += 1
            for i in range(1, len(des_s3_chr_bind)):
                if des_s3_chr_bind[i] == des_s3_chr_bind[i - 1]:
                    continue
                else:
                    if des_s3_chr_bind[i] == 1:
                        n += 1
                    else:
                        m += 1
            # print(des_s3_chr_bind, n, m)
            if abs(m - n) > 1 or n == 0 or m == 0:
                return False
        return is_interleave


if __name__ == '__main__':
    s = Solution()
    s1 = "abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
    s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
    s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
    print(s.isInterleave(s1, s2, s3))
