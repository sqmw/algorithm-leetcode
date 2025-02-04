from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        T(n): O(n)
        S(n): O(1)

        0 1 // 2 -> 1
        0 1 2 // 3 -> 1
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = Solution()
    s = ['0', '1', '2']
    solution.reverseString(s)
    print(s)
