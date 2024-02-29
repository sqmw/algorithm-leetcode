class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        :param n:
        :return:
        """
        one_cou: int = 0
        for i in range(31, -1, -1):
            radix = 2 ** i
            if n // radix == 1:
                one_cou += 1
                n -= radix
        return one_cou


"""
11111111111111111111111111111101 
"""

if __name__ == "__main__":
    print(Solution().hammingWeight(0b11111111111111111111111111111111))
