import collections
from typing import List, Dict


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        这里属于排列，需要考虑顺序的
        1: 1
        2: 1,1   2
        3: 1,1,1   2,1   1,2  3
        4: 1,1,1,1
        method1: 回溯枚举
            T(n): O(n**k)
            S(n): (k)
        method2: 使用动态规划，使用 cache，考虑成树的结构(这种方法比直接循环的更加难以理解)
            T(n): O(n * k)
            S(n): O(k)
            下面是使用 cache_dp 实现的
        """
        val_set: Dict[int, int] = collections.defaultdict(int)

        def cache_dp(_need: int) -> int:
            nonlocal val_set
            if _need < 0:
                return 0
            # if _need == val_min or _need == 0:
            # 其实使用现在的这个就可以了
            if _need == 0:
                return 1
            if _need in val_set:
                return val_set[_need]
            # 取出的事左边的数字
            _tmp_cou = 0
            for num in nums:
                # 左边的数字已经固定(并且左边的数字都是在 nums 里面取出来)，右边的数字 是 _need - num 的所有组成
                _tmp_cou += cache_dp(_need - num)
            val_set[_need] = _tmp_cou
            return _tmp_cou

        return cache_dp(target)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([4, 2, 1], 32))
