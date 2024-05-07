class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))
