class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        T(n): O(n)
        S(n): O(1)
        :param s:
        :return:
        """
        s = s.lower()
        left = 0
        right = len(s) - 1
        while True:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            if left >= right:
                break
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(' '))
