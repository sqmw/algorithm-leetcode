from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        # 表示的是最短的公共前缀的长度
        prefixLen = 0
        while True:
            for i in range(0, len(strs) - 1):
                # 判定长度为 prefixLen 是否符合要求
                if strs[i][0:prefixLen + 1] != strs[i + 1][0:prefixLen + 1]:
                    return strs[0][0:prefixLen]
                if len(strs[i]) <= prefixLen or len(strs[i + 1]) <= prefixLen:
                    return strs[0][0:prefixLen]
            prefixLen += 1


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["", "", '']))
