from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        method1: 转化为二进制，数二进制里面的 1 的个数，性能一般，属于较优解
        T(n): O(nlog(n))
        S(n): O(n)
        """
        des_arr: List[int] = []
        for i in range(n + 1):
            des_arr.append(bin(i).count('1'))
        return des_arr


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5))
