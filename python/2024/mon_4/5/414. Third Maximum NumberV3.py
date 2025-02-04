import random
import sys
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        method2:
            1. 使用贪心思想，维护一个长度为 3 的有升序排序的当前最大数组，一次遍历即可，本质和 V2 一样
            2. 里面的 三个 if else 可以使用 for 循环取代
        T(n): O(n)
        S(n): O(1)
        """
        sorted_first2third: List[int] = [-sys.maxsize, -sys.maxsize + 1, -sys.maxsize + 2]
        for num in nums:
            # 先判定是否在里面
            if num not in sorted_first2third:
                if sorted_first2third[0] < num < sorted_first2third[1]:
                    sorted_first2third[0] = num
                elif sorted_first2third[1] < num < sorted_first2third[2]:
                    del sorted_first2third[0]
                    sorted_first2third.insert(1, num)
                elif num > sorted_first2third[2]:
                    del sorted_first2third[0]
                    sorted_first2third.append(num)
        return sorted_first2third[0] if min(sorted_first2third) > -sys.maxsize + 2 else max(sorted_first2third)


if __name__ == "__main__":
    s = Solution()
    print(s.thirdMax([random.randint(1, 1000000) for _ in range(10000000)]))
