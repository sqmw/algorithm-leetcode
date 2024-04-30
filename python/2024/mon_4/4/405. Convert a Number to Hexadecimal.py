from typing import Dict


class Solution:
    def toHex(self, num: int) -> str:
        # @formatter:off
        hex_decimal_dic: Dict[int, str] = {0:'0', 1:'1',2: '2',3: '3',4: '4',5: '5',6: '6',7: '7',8: '8',9: '9',10: 'a',11: 'b',12: 'c',13: 'd',14: 'e',15: 'f'}
        # @formatter:on
        des_str = ''
        num_is_negative = False
        if num < 0:
            num_is_negative = True
            num = -num
        reverse_need = []
        while num > 0:
            reverse_need.append(num & 1)
            num = num >> 1
        reverse_need.reverse()
        reverse_need = ([0] * (32 - len(reverse_need))) + reverse_need
        if num_is_negative:
            reverse_need[0] = 1
            # 按位取反
            for i in range(1, 32):
                reverse_need[i] = 1 - reverse_need[i]
            # 末位加一
            carry = 1
            for i in range(31, 0, -1):
                new_val = carry ^ reverse_need[i]
                new_carry = carry & reverse_need[i]
                reverse_need[i] = new_val
                carry = new_carry
        for i in range(0, 32, 4):
            _val = reverse_need[i] * 8 + reverse_need[i + 1] * 4 + reverse_need[i + 2] * 2 + reverse_need[i + 3] * 1
            des_str += hex_decimal_dic[_val]
        des_str = des_str.lstrip('0')
        return des_str if des_str != '' else '0'


if __name__ == "__main__":
    s = Solution()
    print(s.toHex(-1))
