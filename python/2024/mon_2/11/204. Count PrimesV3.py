import math
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        S(n): O(n)
        T(n): O(n(log(log n))):
        :param n:
        :return:
        """
        if n < 3:
            return 0
        val_isprime_list: List[bool] = [True] * n
        val_isprime_list[0] = val_isprime_list[1] = False
        for i in range(2, math.floor(n ** 0.5) + 1):
            if val_isprime_list[i] is True:
                # 这里使用 i * i 避免了重复标记
                for j in range(i * i, n, i):
                    val_isprime_list[j] = False
        return sum(val_isprime_list)


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(5000000))
