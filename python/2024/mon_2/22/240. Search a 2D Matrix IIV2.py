from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        根据数据的特性划分为多次的一维的二分
        T(n): O(min(m,n)*log(max(m,n)))
        S(n): O(1)
        """
        row_cou = len(matrix)
        column_cou = len(matrix[0])

        for i in range(row_cou):
            left = 0
            right = column_cou - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 20
    print(s.searchMatrix(matrix, target))
