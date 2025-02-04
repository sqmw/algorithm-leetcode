from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        f: List[int] = [0] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            f[i] = i * f[i - 1] + (i - 2)
        return f[n]
