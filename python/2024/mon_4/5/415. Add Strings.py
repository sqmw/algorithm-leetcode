from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        :param num1:
        :param num2:
        :return:
        T(n): O(n + m)
        S(n): O(max(n,m))
        """
        des_reverse: List[str] = []
        carry = 0
        # 保证 num1_len > num2_len
        #   123
        # +  11
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for i in range(len(num2)):
            digit_num2: int = int(num2[len(num2) - 1 - i])
            digit_num1: int = int(num1[len(num1) - 1 - i])
            des_reverse.append(str((digit_num1 + digit_num2 + carry) % 10))
            carry = (digit_num1 + digit_num2 + carry) // 10
        for i in range(len(num2), len(num1)):
            des_reverse.append(str((int(num1[len(num1) - 1 - i]) + carry) % 10))
            carry = (int(num1[len(num1) - 1 - i]) + carry) // 10
        if carry != 0:
            des_reverse.append(str(carry))
        des_reverse.reverse()

        return ''.join(des_reverse)


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings('11', '123'))
