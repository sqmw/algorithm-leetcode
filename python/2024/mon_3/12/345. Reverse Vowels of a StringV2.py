from typing import Set, List


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        method2:
        T(n): O(n)
        S(n): O(n)
        """
        vowel_set: Set = {'a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U', }
        s_list: List[str] = list(s)
        left = 0
        right = len(s_list) - 1
        while left < right:
            while left < right and s_list[left] not in vowel_set:
                left += 1
            while right > left and s_list[right] not in vowel_set:
                right -= 1
            s_list[right], s_list[left] = s_list[left], s_list[right]
            left += 1
            right -= 1
        return ''.join(s_list)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels('leetcode'))
