import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        method1(使用字典):
            T(n): O(n)
            S(n): O(distinct char_in_s)
        method2(没有显式使用字典，但是使用了字典的性质):
            因为每个字母都是映射一个对应的 ASCII 码，并且是递增的，因此就可以使用一个长度为 26
            的 list 来存储，这个时候就可以直接映射了，数组存储的值就是对应的出现的次数
            T(n): O(n)
            S(n): O(distinct char_in_s)
        官方的所谓的使用队列来实现，实际上和上面的这种是一样的
        """
        char_counter = collections.Counter(s)
        for i in range(len(s)):
            if char_counter[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar('leetcode'))
