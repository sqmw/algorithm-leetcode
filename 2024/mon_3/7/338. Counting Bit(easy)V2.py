from typing import List


# 将模块动态导入
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        method2: 使用动态规划实现
        T(n): O(n)
        S(n): O(n)
        """
        rec_f: List[int] = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            if i % 2 == 0:
                rec_f[i] = rec_f[i // 2]
            else:
                rec_f[i] = rec_f[i - 1] + 1
        return rec_f


if __name__ == "__main__":
    s = Solution()
    for i in range(10000):
        s.countBits(i)
        # print(s.countBits(i))
