from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        des_arr: List[int] = []
        for i in range(n + 1):
            des_arr.append(bin(i).count('1'))
        return des_arr


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5))
