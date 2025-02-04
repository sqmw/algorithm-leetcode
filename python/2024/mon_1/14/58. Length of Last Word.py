class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        def is_letter(c: str) -> bool:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                return True
            return False

        last_index = -1
        for i in range(len(s) - 1, -1, -1):
            if is_letter(s[i]):
                if last_index == -1:
                    last_index = i
            else:
                if last_index != -1:
                    return last_index - i
        return last_index + 1


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("HelloWorld"))
