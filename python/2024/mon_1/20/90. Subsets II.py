from typing import List

"""
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def traceback(_start_index, need: int):
            if need == 0:
                if path not in des_arr_list:
                    des_arr_list.append(path[:])
            else:
                for i in range(_start_index, len(nums)):
                    if len(nums) - i >= need:
                        path.append(nums[i])
                        traceback(1 + i, need - 1)
                        path.pop()

        start_index = 0
        path: List[int] = []
        des_arr_list: List[List[int]] = []
        for i in range(len(nums) + 1):
            traceback(start_index, need=i)
        return des_arr_list


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 3, 5, 6, 7]))
