from typing import List


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        T(n): O(n/1 + n/2 + n/3 + n/4 + n/5 + ... + n/n) == O(nlog(n))
        S(n): O(n)
        """
        bulbs: List[int] = [False] * n
        for i in range(1, n + 1):
            j = i - 1
            while j < n:
                bulbs[j] = not bulbs[j]
                j += i

        return sum(bulbs)


if __name__ == "__main__":
    s = Solution()
    print(s.bulbSwitch(9999999))
