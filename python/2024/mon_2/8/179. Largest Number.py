import functools
from typing import List, Dict


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(str_x: str, str_y: str):
            return int(str_y + str_x) - int(str_x + str_y)

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(cmp))
        res = ''.join(nums)
        res = res.lstrip('0')
        if res == '':
            return '0'
        return res


if __name__ == '__main__':
    nums = [0, 0]
    print(Solution().largestNumber(nums))
