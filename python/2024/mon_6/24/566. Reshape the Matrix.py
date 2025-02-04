from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        init_row = len(mat)
        init_col = len(mat[0])

        if r * c != init_row * init_col:
            return mat
        des_matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(init_row):
            for j in range(init_col):
                # 表示下一个需要填充的一维位置
                total_cou = init_col * i + j
                _i = total_cou // c
                _j = total_cou % c
                des_matrix[_i][_j] = mat[i][j]

        return des_matrix


if __name__ == "__main__":
    s = Solution()
    print(s.matrixReshape([[1,2]], 1, 1))
