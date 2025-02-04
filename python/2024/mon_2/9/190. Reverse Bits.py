"""
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        b_str = bin(n)[2:]
        b_str = b_str.rjust(32, '0')  # // str.padLeft(width, padding)
        b_str = b_str[::-1]
        b_str = b_str.lstrip('0')
        if b_str == '':
            return 0
        return int(b_str, 2)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(0b00000000000000000000000000000000))
