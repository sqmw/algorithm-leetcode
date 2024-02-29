from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # k:v   'num: num_cou' 等于 2 就移除
        num_dic: dict[int, int] = {}

        for item in nums:
            if item in num_dic:
                del num_dic[item]
            else:
                num_dic[item] = 1
        return list(num_dic.keys())[0]


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))
