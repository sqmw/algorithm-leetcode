import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        T(n): O(n ** 0.5)
        S(n): O(1)
        """
        W: int = math.floor(area ** 0.5)
        while area % W != 0:
            W -= 1
        return [area // W, W]


if __name__ == "__main__":
    s = Solution()
    print(s.constructRectangle(2))
