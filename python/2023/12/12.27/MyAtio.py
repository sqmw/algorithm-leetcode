def isBaseTen(c: str) -> bool:
    if ord('0') <= ord(c) <= ord('9'):
        return True
    return False


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if len(s) == 0:
            return 0
        start = 0
        _sum = 0
        isPositiveNum = True
        numLen = 0
        if s[0] == '+':
            start = 1
        if s[0] == '-':
            isPositiveNum = False
            start = 1
        if s[0] != '+' and s[0] != '-' and not isBaseTen(s[0]):
            return 0
        for i in range(start, len(s)):
            if isBaseTen(s[i]):
                numLen += 1
            else:
                break
        for i in range(0, numLen):
            _sum += int(s[start + i]) * 10 ** (numLen - i - 1)
        if not isPositiveNum:
            _sum = -_sum
        if _sum < -2**31:
            return -2**31
        if _sum > 2**31 - 1:
            return 2**31 - 1
        return _sum
