import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        判定 ransomNode 是否可以由 magazine 组成
        method1:
            通过字典来计数，判定是否组成 ransomNode 的 char 都可以在 magazine 里面找到
        T(n): O(magazine_len)
        S(n): O(count(distinct_char in magazine))
        method2:
            通过将两个字符串都进行排序，依次判定 ransomNote 里面的字符是否都可以在 magazine 里面找到
            T(n): O(nlog(n))
            S(n): O(1)
        """
        if len(magazine) < len(ransomNote):
            return False
        magazine_counter = collections.Counter(magazine)
        for char in ransomNote:
            magazine_counter[char] -= 1
            if magazine_counter[char] < 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct('aaa', 'aaba'))
