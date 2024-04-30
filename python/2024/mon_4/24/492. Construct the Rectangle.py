import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        T(n): O(n ** 0.5)
        S(n): O(1)
        """
        L: int = math.ceil(area ** 0.5)
        while area % L != 0:
            L += 1
        return [L, area // L]


if __name__ == "__main__":
    s = Solution()
    print(s.constructRectangle(2))
