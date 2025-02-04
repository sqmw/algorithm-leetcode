class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_num = str(x)
        end = int(len(s_num) / 2 - 1)
        for i in range(0, end + 1):
            if s_num[i] != s_num[len(s_num) - 1 - i]:
                return False
        return True
