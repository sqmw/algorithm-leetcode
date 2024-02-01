from typing import List


def reverse(self, x: int) -> int:
    isPositiveNum = True
    if x < 0:
        isPositiveNum = False
        x = -x
    _sum = 0
    digitNums = []
    while x != 0:
        tail: int = x % 10
        digitNums.append(int(tail))
        x = (x - tail) / 10
        print(digitNums)
    for i in range(0, len(digitNums)):
        _sum += digitNums[i] * 10 ** (len(digitNums) - i - 1)
    if not isPositiveNum:
        _sum = -_sum
    if _sum > 2 ** 31 - 1 or _sum < - 2 ** 31:
        return 0
    return _sum

print(reverse(0, -123))
