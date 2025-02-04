from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        des_arr: List[List[int]] = []
        path: List[int] = []

        def traceback(start, _init_need: int, _now_need: int):
            if _now_need == 0:
                des_arr.append(path[:])
            else:
                for i in range(start, len(nums)):
                    if len(nums) - i >= _now_need:
                        if len(path) == 0 or nums[i] > path[len(path) - 1]:
                            path.append(nums[i])
                            traceback(start + 1, _init_need, _now_need - 1)
                            path.pop()

        set_len = 0
        while set_len <= len(nums):
            traceback(0, _init_need=set_len, _now_need=set_len)
            set_len += 1
        return des_arr


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3, 4, 5]))
