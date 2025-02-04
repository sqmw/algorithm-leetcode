from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        add_list: List[List[int]] = []
        max_len_add = 0
        sum_list = []
        # 保证 len(num1) <= len(num2)
        if len(num1) > len(num2):
            t = num1
            num1 = num2
            num2 = t
        if num1 == '0':
            return '0'
        for i in range(len(num1) - 1, -1, -1):
            add = [0 for _ in range(0, len(num1) - 1 - i)]  # 反过来记录
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                add.append((int(num1[i]) * int(num2[j]) + carry) % 10)
                carry = int((int(num1[i]) * int(num2[j]) + carry) / 10)
            if carry != 0:
                add.append(carry)
            if max_len_add < len(add):
                max_len_add = len(add)
            add_list.append(add)
        carry = 0
        print(add_list)
        for i in range(0, max_len_add):
            _sum = 0
            for j in range(0, len(add_list)):
                if i < len(add_list[j]):
                    _sum += add_list[j][i]
            sum_list.append((_sum + carry) % 10)
            carry = int((_sum + carry)/ 10)
        if carry != 0:
            sum_list.append(carry)
        print(sum_list)
        sum_list.reverse()
        return ''.join([str(item) for item in sum_list])


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("999", "0"))
