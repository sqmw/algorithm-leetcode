class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        method1:
            >>
            T(n): O(log(n))
            S(n): O(1)
        """
        des_xor: int = x ^ y
        des_diff_cou: int = 0

        # 计算 1 的数量
        while des_xor != 0:
            des_diff_cou += (des_xor & 1)
            des_xor >>= 1
        return des_diff_cou


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1, 4))
