from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 需要保证 a <= b a > 0 b > 0
        if m > n:
            t = m
            m = n
            n = t
        if m == 1:
            return 1
        if m == 2:
            return n
        times_list: List[int] = [1 for _ in range(n)]
        for i in range(m - 1 - 1):
            temp = times_list[:]
            for j in range(n):
                times_list[j] = sum(temp[:j + 1])
        return sum(times_list)


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(10, 38))  # 548354040
