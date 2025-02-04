class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        T(n): O(n)
        S(n): O(1)
        """
        des_str: str = ''
        des_str += s[k - 1:None:-1]
        des_str += s[k: 2 * k]
        for i in range(2 * k, len(s), 2 * k):
            des_str += s[i + k - 1:i - 1:-1]
            des_str += s[i + k: i + 2 * k]
        return des_str


if __name__ == "__main__":
    s = Solution()
    print(s.reverseStr('abcdefg', 2))
