class Solution:
    def findComplement(self, num: int) -> int:
        bin_str_list = list(bin(num)[2:])
        for i in range(len(bin_str_list)):
            if bin_str_list[i] == '1':
                bin_str_list[i] = '0'
            else:
                bin_str_list[i] = '1'
        return int(''.join(bin_str_list), 2)


if __name__ == "__main__":
    s = Solution()
    print(s.findComplement(5))
