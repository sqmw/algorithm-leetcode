from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        T(n): O(1)
        S(n): O(1)
        """
        if n == 0:
            return False
        return n & (n - 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(0))
