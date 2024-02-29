class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        des_num: int = 0
        for i in range(len(columnTitle)):
            des_num += (ord(columnTitle[len(columnTitle) - 1 - i]) - ord('A') + 1) * (26 ** i)
        return des_num


if __name__ == "__main__":
    print(Solution().titleToNumber('ZY'))
