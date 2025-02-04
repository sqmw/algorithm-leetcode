import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dic: dict[int, int] = collections.defaultdict(lambda: 0)
        for item in nums:
            if num_dic[item] == 2:
                del num_dic[item]
            else:
                num_dic[item] += 1
        return list(num_dic.keys())[0]


if __name__ == "__main__":
    print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
