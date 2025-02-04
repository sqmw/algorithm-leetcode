import copy
from typing import List


class NumMatrix:
    """
    T(n): O(1)
    S(n): O(row * column)

    method1：通过动态规划的思想构造出对应的 (0,0) 到 目的地 (i, j) 的 sum
             之后即可通过数学表达式求出 des_sum
    """

    def __init__(self, matrix: List[List[int]]):
        # 实际上可以在原数组上面进行修改即可，但是这样坑不符合实际情况
        self.rec_f: List[List[int]] = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.rec_f[i][j] += (self.rec_f[i][j - 1] if j > 0 else 0) + \
                                    (self.rec_f[i - 1][j] if i > 0 else 0) - \
                                    (self.rec_f[i - 1][j - 1] if i > 0 and j > 0 else 0)

    # @formatter:off
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def get_rec_f_val(_i: int, _j : int):
            if _i > -1 and _j > -1:
                return self.rec_f[_i][_j]
            else:
                return 0
        return get_rec_f_val(row2, col2) - get_rec_f_val(row1 - 1, col2) - get_rec_f_val(row2, col1 - 1) + \
            get_rec_f_val(row1 - 1, col1 - 1)
        # 这里为什么是错的, 使用 val if condition else XXX 的时候要使用括号，下面的就是正确的
        # return (self.rec_f[row2][col2]) -\
        #        (self.rec_f[row1 - 1][col2] if row1 > 0 else 0) -\
        #        (self.rec_f[row2][col1 - 1] if col1 > 0 else 0) +\
        #        (self.rec_f[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)
    # @formatter:on


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    """
    input: 
    [2, 1, 4, 3], 
    [1, 1, 2, 2],
    [1, 2, 2, 4]
    output: 
    [8, 11, 12]
    """
    matrix = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(2, 1, 4, 3))
