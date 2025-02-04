from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        f: List[List[int]] = []
        for i in range(len(triangle)):
            # 初始化改行，之后在进行赋值
            f.append([0 for _ in range(len(triangle[i]))])
            for j in range(len(triangle[i])):
                # 这里需要调整
                if i == 0:
                    f[0][0] = triangle[0][0]
                elif j == 0:
                    f[i][j] = triangle[i][j] + f[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    f[i][j] = triangle[i][j] + f[i - 1][j - 1]
                else:
                    f[i][j] = triangle[i][j] + min(f[i - 1][j - 1], f[i - 1][j])

        return min(f[len(f) - 1])


if __name__ == "__main__":
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
                                  ))
