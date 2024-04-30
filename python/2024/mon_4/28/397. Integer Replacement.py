import collections
from typing import Dict


class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        method1:
            使用动态规划,记忆化搜索
            T(n): O(log(n))
            S(n): O(log(n))
        method2:
            使用贪心算法求解
        这里使用了 method1
        """
        _cache_dic: Dict[int, int] = collections.defaultdict(int)

        def cache_recurse(_n: int) -> int:
            if _n == 1:
                _cache_dic[_n] = 0
                return 0
            if _n in _cache_dic:
                return _cache_dic[_n]
            if _n % 2 == 0:
                _cache_dic[_n] = cache_recurse(_n // 2) + 1
            else:
                _cache_dic[_n] = min(cache_recurse(_n - 1), cache_recurse(_n + 1)) + 1
            return _cache_dic[_n]

        return cache_recurse(n)


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 1000):
        print(f'{i}: {s.integerReplacement(i)}', end='\t')
