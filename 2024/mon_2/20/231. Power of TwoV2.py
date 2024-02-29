from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow2list: List[int] = [1, 2, 4, 8, 2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7, 2 ** 8]
        ...


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo())
