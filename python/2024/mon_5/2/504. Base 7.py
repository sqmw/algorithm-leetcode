from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        T(n): O(n)
        S(n): O(n)
        """
        negative = False
        if num < 0:
            negative = True
            num = -num
        dividend = num
        _stack: List[str] = []
        while dividend != 0:
            surplus = dividend % 7
            _stack.append(str(surplus))
            dividend = dividend // 7
        if negative:
            _stack.append("-")
        _stack.reverse()

        return "".join(_stack) if len(_stack) > 0 else "0"


if __name__ == "__main__":
    s = Solution()
    print(s.convertToBase7(100))
