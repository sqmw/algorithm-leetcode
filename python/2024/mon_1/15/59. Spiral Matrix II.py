import math
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # des_arr: List[List[int]] = []
        # 初始化 Matrix
        des_arr = [[0 for _ in range(n)] for _ in range(n)]
        T = int(math.ceil(n / 2))
        t = 1  # 表示现在是第一周期
        i = j = 0
        start = 1
        while t <= T:

            # left->right
            for k in range(n - 2 * t + 1):
                des_arr[i][j] = start
                start += 1
                j += 1
            # top->bottom
            for k in range(n - 2 * t + 1):
                des_arr[i][j] = start
                start += 1
                i += 1
            # l -> r
            for k in range(n - 2 * t + 1):
                des_arr[i][j] = start
                start += 1
                j -= 1
            # b -> t
            for k in range(n - 2 * t + 1):
                des_arr[i][j] = start
                start += 1
                i -= 1
            i += 1
            j += 1
            t += 1
        # 添加最后一个中间的数
        if n % 2 == 1:
            des_arr[i - 1][j - 1] = n * n
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1))
