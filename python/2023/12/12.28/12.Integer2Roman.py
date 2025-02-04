"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    roman = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I',
    }

    special = {
        900: 'CM',
        400: 'CD',
        90: 'XC',
        40: 'XL',
        9: 'IX',
        4: 'IV',
    }

    def intToRoman(self, num: int) -> str:
        v_times_map_list = []
        str_list = []
        for k in self.roman.keys():
            roman_v = int(num / k)
            num -= roman_v * k
            v_times_map_list.append((k, roman_v))
        print(v_times_map_list)
        i = 0
        while i < len(v_times_map_list):
            if i + 1 < len(v_times_map_list):
                replace_str = self.special.get(
                    v_times_map_list[i][0] * v_times_map_list[i][1] + v_times_map_list[i + 1][0] *
                    v_times_map_list[i + 1][1])
            else:
                replace_str = None
            if replace_str is not None:
                str_list.append(replace_str)
                i += 2
            else:
                temp_str = ''
                roman_v = v_times_map_list[i][0]
                for j in range(0, v_times_map_list[i][1]):
                    temp_str += self.roman.get(roman_v)
                str_list.append(temp_str)
                i += 1
        des_str = ''
        for item in str_list:
            des_str += item
        return des_str


s = Solution()
#print(s.intToRoman(1994))  # "MCMXCIV"
print(s.intToRoman(4))  # "MCMXCIV"
