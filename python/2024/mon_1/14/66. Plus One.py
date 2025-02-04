from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        des_arr: List[int] = []
        for i in range(len(digits) - 1, -1, -1):
            des_arr.append((carry + digits[i])%10)
            carry = (carry + digits[i]) // 10
        if carry != 0:
            des_arr.append(carry)
        des_arr.reverse()
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9, 9]))
