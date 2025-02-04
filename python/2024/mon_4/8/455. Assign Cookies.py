from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        使用 排序&双指针 实现
        T(n): O(nlog(n) + mlog(m))
        S(n): O(max(nlog(n), mlog(m)))
        """
        g.sort()
        s.sort()
        child_index = 0
        cookie_index = 0
        while child_index < len(g) and cookie_index < len(s):
            if g[child_index] <= s[cookie_index]:
                child_index += 1
                cookie_index += 1
            # g[child_index] > s[cookie_index]
            else:
                cookie_index += 1

        return min(cookie_index, child_index)


if __name__ == "__main__":
    s = Solution()
    print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
