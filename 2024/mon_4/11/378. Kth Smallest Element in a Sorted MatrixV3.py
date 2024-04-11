from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        再次读一遍题目，才会发现 row 和 column 都是非降序的，所以就可以充分利用题目给的信息
        T(n): O(n*(log(_max - _min)))
        S(n): O(1)
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            # 开始计数
            cou = 0
            # 注意这里的 j 的位置
            j = len(matrix) - 1
            for i in range(len(matrix)):
                while j > -1 and matrix[i][j] > mid:
                    j -= 1
                cou += (j + 1)
            if cou < k:
                left = mid + 1
            else:
                right = mid
        return left  # 其实就是 mid


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix=[[1, 5, 9],
                                [10, 11, 13],
                                [12, 13, 15]], k=8))
