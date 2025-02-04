class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        :param n:
        :return:
        """
        one_cou: int = 0
        binary_num_str: str = bin(n)[2:]
        for item in binary_num_str:
            if item == '1':
                one_cou += 1
        return one_cou


"""
11111111111111111111111111111101 
"""

if __name__ == "__main__":
    print(Solution().hammingWeight(0b11111111111111111111111111111111))
