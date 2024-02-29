import sys
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        method1: 使用动态规划思想...需要排序
        method2: 借助 map hash实现
            T(n): O(n)
        :param nums:
        :return:
        """
        # bool 表示是否被查看过，被查看过就直接跳过
        num_dic: [int, bool] = {}
        for item in nums:
            num_dic[item] = False
        max_len = 0
        for k in num_dic.keys():
            now_len = 0
            if num_dic[k] is True:
                continue
            else:
                now_len += 1
                num_dic[k] = True
                # 先左边找
                i = k - 1
                while i in num_dic:
                    num_dic[i] = True
                    now_len += 1
                    i -= 1
                # 再右边找
                i = k + 1
                while i in num_dic:
                    num_dic[i] = True
                    now_len += 1
                    i += 1
                max_len = max(max_len, now_len)

        return max_len


if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
