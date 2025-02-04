class Solution:
    def reverseWords(self, s: str) -> str:
        """
        T(n): O(n)
        S(n): O(n)
        :param s:
        :return:
        """
        split_s = s.split(' ')
        for i in range(len(split_s)):
            split_s[i] = split_s[i][len(split_s[i]) - 1:None:-1]
        return ' '.join(split_s)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
