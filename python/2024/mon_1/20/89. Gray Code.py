from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return []
        des_arr: List[int] = [0]

        # i 表示现在的位数
        for i in range(1, n + 1):
            _sum = 2 ** (i - 1)
            for j in range(2 ** (i - 1) - 1, -1, -1):
                des_arr.append(_sum + des_arr[j])

        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(1))  # [0,1,3,2,6,7,5,4]
