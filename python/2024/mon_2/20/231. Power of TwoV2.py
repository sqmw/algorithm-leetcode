from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        T(n): O(n)
        S(n): O(log(n))
        """
        if n == 0:
            return False
        b_num_str = bin(n)
        for i in range(3, len(b_num_str)):
            if b_num_str[i] == '1':
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(0))
