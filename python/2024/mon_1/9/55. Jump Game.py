from typing import List

"""
通过遍历0，查看0是否可以度过实现
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_index_arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                # 连续的0，仅仅加入最后一个
                if (i + 1 < len(nums) and nums[i + 1] != 0) or i + 1 >= len(nums):
                    zero_index_arr.append(i)
        if nums[0] == 0 and len(nums) > 1:
            return False
        if len(zero_index_arr) == 0 or len(nums) == 1:
            return True
        end_index = 0
        zero_index_arr_index = 0
        start_index = zero_index_arr[zero_index_arr_index]
        while True:
            if start_index == len(nums) - 1 and (start_index > -1 and nums[start_index - 1] != 0):
                return True
            can_pass = False
            for i in range(start_index - 1, end_index - 1, -1):
                if nums[i] >= start_index - i + 1 or (
                        start_index == len(nums) - 1 and nums[i] >= start_index - i):  # >=
                    can_pass = True
            if not can_pass:
                for i in range(end_index - 1, -1, -1):
                    if nums[i] >= start_index - i + 1 or (
                            start_index == len(nums) - 1 and nums[i] >= start_index - i):  # >=
                        can_pass = True
                if not can_pass:
                    return False
            end_index = start_index + 1
            zero_index_arr_index += 1
            if zero_index_arr_index >= len(zero_index_arr):
                break
            start_index = zero_index_arr[zero_index_arr_index]
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump(
        [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7,
         0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6,
         7, 5, 1, 9, 9, 3, 5, 0, 7, 5]))
