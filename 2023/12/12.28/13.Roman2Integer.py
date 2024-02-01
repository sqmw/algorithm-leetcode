class Solution:
    roman = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
    }

    special = {
        'CM': 900,
        'CD': 400,
        'XC': 90,
        'XL': 40,
        'IX': 9,
        'IV': 4,
    }

    def romanToInt(self, s: str) -> int:
        _sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s):
                int_val = self.special.get(s[i:i + 2])
            else:
                int_val = None
            if int_val is not None:
                _sum += int_val
                i += 2
            else:
                _sum += self.roman.get(s[i])
                i += 1

        return _sum


s = Solution()
print(s.romanToInt("MCMXCIV"))
