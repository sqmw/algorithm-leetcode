"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
"""
from typing import List


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        实际上是26进位制，数字的开始是 1，不是 0
        :param columnNumber:
        :return:
        """
        reverse_str_list: List[str] = []
        while columnNumber != 0:
            if columnNumber <= 26:
                reverse_str_list.append(chr(ord('A') - 1 + columnNumber))
                break
            else:
                if columnNumber % 26 == 0:
                    reverse_str_list.append('Z')
                    columnNumber = columnNumber // 26 - 1
                else:
                    reverse_str_list.append(chr(ord('A') - 1 + columnNumber % 26))
                    columnNumber = columnNumber // 26

        reverse_str_list.reverse()
        return ''.join(reverse_str_list)


if __name__ == "__main__":
    print(Solution().convertToTitle(28))

