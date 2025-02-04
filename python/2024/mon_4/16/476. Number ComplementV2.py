class Solution:
    def findComplement(self, num: int) -> int:
        _bin_len = 0
        init_num = num
        while init_num != 0:
            _bin_len += 1
            init_num >>= 1
        return (2 ** _bin_len) - 1 - num


if __name__ == "__main__":
    s = Solution()
    print(s.findComplement(5))
