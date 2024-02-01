class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        index_s = 0
        while index_s <= len(haystack) - len(needle):
            index_pattern = 0
            while index_pattern < len(needle):
                if haystack[index_s + index_pattern] != needle[index_pattern]:
                    break
                else:
                    if index_pattern == len(needle) - 1:
                        return index_s
                index_pattern += 1
            index_s += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("adbutsad", 'sad'))
