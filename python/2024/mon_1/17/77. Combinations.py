from typing import List
"""
这个问题有两个解法：
    一种非递归循环实现，需要使用两个指针(index)，但是实现复杂
    一种是递归实现，也就是回溯法
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        组合问题
        :param n:
        :param k:
        :return:
        """
        def traceback(_n: int, _need: int):
            if _need == 0:
                des_arr.append(path[:])
            else:  # len = _n - _need
                for i in range(0, _n - _need + 1):
                    path.append(_n - i)
                    traceback(_n - i - 1, _need - 1)
                    path.pop()
        path = []
        des_arr: List[List[int]] = []
        traceback(n, k)
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.combine(100, 0))
