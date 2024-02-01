from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m 行
        m = len(matrix)
        # n 列
        n = len(matrix[0])
        des_arr: List[int] = []
        i = j = 0
        # 表示第一周期
        t = 0
        while len(des_arr) < m * n:
            if len(des_arr) + 1 == m * n:
                des_arr.append(matrix[i][j])
            # 这里是第一个起点，一定存在
            for p in range(i, n - 1 - t):
                des_arr.append(matrix[i][p])
            for p in range(j, m - 1 - t):
                des_arr.append(matrix[p][n - 1 - t])
            for p in range(n - 1 - t, j, -1):
                des_arr.append(matrix[m - 1 - t][p])
            for p in range(m - 1 - t, i, -1):
                des_arr.append(matrix[p][j])
            if len(des_arr) > m * n:
                des_arr = des_arr[: m * n]
            i += 1
            j += 1
            t += 1

        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[6,9,7]]))
    # [1,2,3,4,8,12,11,10,9,5,6,7]
