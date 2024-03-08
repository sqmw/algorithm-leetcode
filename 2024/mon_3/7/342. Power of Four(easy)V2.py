

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        method2: 1. 二项式展开定理(中学知识)
                 2. 先判定是否是 2 的幂，再判定是否 n % 3 == 1
        T(n): O(1)
        S(n): O(1)
        """
        if n < 1:
            return False
        else:
            return n & (n - 1) == 0 and n % 3 == 1


def t(n: int):
    return (1073741824 / n) % 4 == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(1))

    i = 1
    while i < 2 ** 31:
        assert s.isPowerOfFour(i) == t(i)
