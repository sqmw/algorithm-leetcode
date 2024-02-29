class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_left = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift_left += 1

        right <<= shift_left

        return right


if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(1, 2147483647))
